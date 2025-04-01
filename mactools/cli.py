import click
import subprocess
import sys


@click.group()
def cli():
    """mactools - A CLI tool for managing macOS system settings"""
    pass


@cli.command()
def dock_reset():
    """Reset the Dock to default settings"""
    try:
        # Reset dock tile size to default (64)
        subprocess.run(
            [
                "defaults",
                "write",
                "com.apple.dock",
                "tilesize",
                "-integer",
                "64",
            ],
            check=True,
        )
        # Restart the Dock
        subprocess.run(["killall", "Dock"], check=True)
        click.echo("Dock has been reset to default settings.")
    except subprocess.CalledProcessError as e:
        click.echo(f"Error: Failed to reset dock: {e}", err=True)
        sys.exit(1)


def main():
    cli()


if __name__ == "__main__":
    main()
