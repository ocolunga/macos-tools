import typer
from .commands.dock import dock_app

app = typer.Typer()
app.add_typer(dock_app, name="dock", help="Manage dock settings")


def main():
    app()


if __name__ == "__main__":
    main()
