import typer
import importlib.metadata
from .commands.dock import dock_app
from .commands.keyboard import keyboard_app
from .commands.system import system_app

app = typer.Typer()
app.add_typer(dock_app, name="dock", help="Manage dock settings")
app.add_typer(keyboard_app, name="keyboard", help="Manage keyboard settings")
app.add_typer(system_app, name="system", help="Manage system settings")


def _version_callback(value: bool):
    if value:
        version = importlib.metadata.version("mct")
        typer.echo(f"mct version: {version}")
        raise typer.Exit()


@app.callback()
def callback(
    version: bool = typer.Option(
        False, "--version", "-v", help="Show the version and exit.", callback=_version_callback
    )
):
    """macOS Configuration Tools - Manage macOS system settings."""
    pass


def main():
    app()


if __name__ == "__main__":
    main()
