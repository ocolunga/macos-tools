# macOS Tools

A personal collection of CLI tools for managing macOS settings. This is a work in progress and currently only has basic functionality implemented.

## Features

Currently implemented:
- Dock management
  - Reset dock to default settings (`macos-tools dock reset`)

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
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
