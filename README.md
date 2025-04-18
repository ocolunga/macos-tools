# macOS Tools

A personal collection of CLI tools for managing macOS settings. This is a work in progress and currently only has basic functionality implemented.

## Features

Currently implemented:
- Dock management
  - Reset dock to default settings (`macos-tools dock reset`)
  - Lock dock size to prevent changes (`macos-tools dock lock-size`)
  - Unlock dock size to allow changes (`macos-tools dock unlock-size`)
  - Enable/disable dock autohide (`macos-tools dock autohide [true|false]`)
- Keyboard management
  - Disable press-and-hold for accented characters (`macos-tools keyboard disable-accent-hold`)
  - Enable press-and-hold for accented characters (`macos-tools keyboard enable-accent-hold`)

Planned features:
- More dock management options
- System preferences management
- And more...

## Installation

```bash
# Install using pip
pip install macos-tools

# Or install using uv
uv pip install macos-tools
```

## Usage

```bash
# Show help
macos-tools --help

# Dock management
macos-tools dock --help

# Reset dock to default settings
macos-tools dock reset

# Lock dock size
macos-tools dock lock-size

# Unlock dock size
macos-tools dock unlock-size

# Enable dock autohide
macos-tools dock autohide true

# Disable dock autohide
macos-tools dock autohide false

# Keyboard management
macos-tools keyboard --help

# Disable press-and-hold for accented characters
macos-tools keyboard disable-accent-hold

# Enable press-and-hold for accented characters
macos-tools keyboard enable-accent-hold
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
