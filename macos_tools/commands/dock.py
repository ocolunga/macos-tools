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
