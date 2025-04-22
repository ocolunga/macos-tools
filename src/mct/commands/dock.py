import subprocess
import typer

dock_app = typer.Typer()


@dock_app.command()
def set_size(size: int = typer.Argument(64, help="Size of dock icons")):
    """Set the size of dock icons."""
    try:
        # Set dock size
        subprocess.run(
            [
                "defaults",
                "write",
                "com.apple.dock",
                "tilesize",
                "-integer",
                str(size),
            ],
            check=True,
        )
        # Restart dock
        subprocess.run(["killall", "Dock"], check=True)
        typer.echo(f"Successfully set dock size to {size}")
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error setting dock size: {e}", err=True)


@dock_app.command()
def reset():
    """Reset dock to default size."""
    try:
        # Delete the custom size setting
        subprocess.run(
            [
                "defaults",
                "delete",
                "com.apple.dock",
                "tilesize",
            ],
            check=True,
        )
        # Restart dock
        subprocess.run(["killall", "Dock"], check=True)
        typer.echo("Successfully reset dock to default size")
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error resetting dock: {e}", err=True)


@dock_app.command()
def lock_size():
    """Lock the dock size to prevent changes."""
    try:
        # Make dock size immutable
        subprocess.run(
            [
                "defaults",
                "write",
                "com.apple.dock",
                "size-immutable",
                "-bool",
                "yes",
            ],
            check=True,
        )
        # Restart dock
        subprocess.run(["killall", "Dock"], check=True)
        typer.echo("Successfully locked dock size")
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error locking dock size: {e}", err=True)


@dock_app.command()
def unlock_size():
    """Unlock the dock size to allow changes."""
    try:
        # Make dock size mutable
        subprocess.run(
            [
                "defaults",
                "write",
                "com.apple.dock",
                "size-immutable",
                "-bool",
                "no",
            ],
            check=True,
        )
        # Restart dock
        subprocess.run(["killall", "Dock"], check=True)
        typer.echo("Successfully unlocked dock size")
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error unlocking dock size: {e}", err=True)


@dock_app.command()
def autohide(
    enable: bool = typer.Argument(True, help="Enable or disable autohide"),
):
    """Enable or disable dock autohide."""
    try:
        # Set dock autohide
        subprocess.run(
            [
                "defaults",
                "write",
                "com.apple.dock",
                "autohide",
                "-bool",
                "true" if enable else "false",
            ],
            check=True,
        )
        # Restart dock
        subprocess.run(["killall", "Dock"], check=True)
        typer.echo(
            f"Successfully {'enabled' if enable else 'disabled'} dock autohide"
        )
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error setting dock autohide: {e}", err=True)
