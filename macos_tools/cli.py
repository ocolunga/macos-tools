import typer
from .commands.dock import dock_app
from .commands.keyboard import keyboard_app

app = typer.Typer()
app.add_typer(dock_app, name="dock", help="Manage dock settings")
app.add_typer(keyboard_app, name="keyboard", help="Manage keyboard settings")


def main():
    app()


if __name__ == "__main__":
    main()
