#!/bin/bash

# Create .mct directory in home if it doesn't exist
MCT_DIR="$HOME/.mct"
mkdir -p "$MCT_DIR"
mkdir -p "$MCT_DIR/bin"  # Create a separate bin directory for our scripts

# Use system Python with uv - try different possible locations
if [ -f "/Library/Developer/CommandLineTools/usr/bin/python3" ]; then
    SYSTEM_PYTHON="/Library/Developer/CommandLineTools/usr/bin/python3"
elif [ -f "/usr/bin/python3" ]; then
    SYSTEM_PYTHON="/usr/bin/python3"
else
    echo "Error: Could not find system Python"
    exit 1
fi

uv venv "$MCT_DIR/venv" --python "$SYSTEM_PYTHON"

# Activate the virtual environment
source "$MCT_DIR/venv/bin/activate"

# Install the package in editable mode from the current directory
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