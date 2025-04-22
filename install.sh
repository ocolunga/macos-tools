#!/bin/bash

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check for required commands
for cmd in git python3 curl; do
    if ! command_exists "$cmd"; then
        echo "Error: $cmd is required but not installed"
        exit 1
    fi
done

# Install uv if not present
if ! command_exists uv; then
    echo "Installing uv package manager..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

# Create .mct directory in home if it doesn't exist
MCT_DIR="$HOME/.mct"
mkdir -p "$MCT_DIR"
mkdir -p "$MCT_DIR/bin"  # Create a separate bin directory for our scripts

# Clone the repository if running via curl
REPO_DIR="$MCT_DIR/repo"
if [ ! -d "$REPO_DIR" ]; then
    echo "Cloning mct repository..."
    git clone https://github.com/ocolunga/mct.git "$REPO_DIR"
    cd "$REPO_DIR"
fi

# Use system Python with uv - try different possible locations
if [ -f "/Library/Developer/CommandLineTools/usr/bin/python3" ]; then
    SYSTEM_PYTHON="/Library/Developer/CommandLineTools/usr/bin/python3"
elif [ -f "/usr/bin/python3" ]; then
    SYSTEM_PYTHON="/usr/bin/python3"
else
    echo "Error: Could not find system Python"
    exit 1
fi

# Create and activate virtual environment
uv venv "$MCT_DIR/venv" --python "$SYSTEM_PYTHON"
source "$MCT_DIR/venv/bin/activate"

# Install the package in editable mode
cd "$REPO_DIR"
uv pip install -e .

# Create wrapper scripts for our commands in the separate bin directory
for script in "$MCT_DIR/venv/bin/mct"*; do
    if [ -f "$script" ]; then
        base_name=$(basename "$script")
        cat > "$MCT_DIR/bin/$base_name" << EOF
#!/bin/bash
source "$MCT_DIR/venv/bin/activate"
"$script" "\$@"
EOF
        chmod +x "$MCT_DIR/bin/$base_name"
    fi
done

# Create or update shell configuration
SHELL_CONFIG="$HOME/.zshrc"
if [[ "$SHELL" == *"bash"* ]]; then
    SHELL_CONFIG="$HOME/.bashrc"
fi

# Add only our bin directory to PATH if not already present
MCT_BIN="$MCT_DIR/bin"
if ! grep -q "$MCT_BIN" "$SHELL_CONFIG"; then
    echo "export PATH=\"$MCT_BIN:\$PATH\"" >> "$SHELL_CONFIG"
    echo "Installation complete! Please restart your terminal or run:"
    echo "source $SHELL_CONFIG"
fi