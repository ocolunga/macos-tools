# macOS Configuration Tools (mct)

A personal collection of CLI tools for managing macOS settings through a simple, intuitive interface.

## Features

Currently implemented:

### Dock Management
- Set dock size: `mct dock size <value>` (32-128)
- Show current dock size: `mct dock size`
- Auto-hide controls:
  - `mct dock hide` - Enable auto-hide
  - `mct dock show` - Disable auto-hide
- Size lock controls:
  - `mct dock lock` - Lock dock size
  - `mct dock unlock` - Unlock dock size
- Reset options:
  - `mct dock reset -s` - Reset size to default (64)
  - `mct dock reset -h` - Reset auto-hide to default (disabled)
  - `mct dock reset -l` - Reset size lock to default (unlocked)
  - `mct dock reset -a` - Reset all dock settings
  
### Keyboard Management
- Key repeat controls:
  - `mct keyboard hold` - Enable press-and-hold for accented characters
  - `mct keyboard repeat` - Enable key repeat (disables accents)
- Reset options:
  - `mct keyboard reset -h` - Reset key hold to default (enabled)
  - `mct keyboard reset -a` - Reset all keyboard settings

Planned features:
- More dock management options
- System preferences management
- And more...

## Installation

### Using the install script (recommended)
```bash
# Clone the repository
git clone https://github.com/yourusername/macos-tools.git
cd macos-tools

# Make the script executable and run it
chmod +x install.sh
./install.sh
```

The install script will:
- Create a `.mct` directory in your home folder
- Set up a virtual environment using the system Python
- Install the package in development mode
- Add the package commands to your PATH

After installation, restart your terminal or source your shell configuration file:
```bash
source ~/.zshrc  # for zsh
# or
source ~/.bashrc  # for bash
```

### Alternative installation methods

```bash
# Install using uv
uv pip install mct

# Or install using pip
pip install mct
```

## Usage Examples

```bash
# Show help
mct --help
mct dock --help
mct keyboard --help

# Dock Examples
mct dock size 48          # Set dock size to 48
mct dock size            # Show current dock size
mct dock hide           # Enable auto-hide
mct dock show           # Disable auto-hide
mct dock lock           # Lock dock size
mct dock unlock         # Unlock dock size
mct dock reset -s -h    # Reset both size and auto-hide

# Keyboard Examples
mct keyboard hold      # Enable press-and-hold for accents
mct keyboard repeat    # Enable key repeat (disable accents)
mct keyboard reset -a  # Reset all keyboard settings
```

Note: Some commands may require restarting applications to take effect.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
