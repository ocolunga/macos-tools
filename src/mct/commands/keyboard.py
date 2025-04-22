import typer
import subprocess

keyboard_app = typer.Typer()

@keyboard_app.command()
def hold():
    """Enable key hold for accented characters."""
    try:
        subprocess.run(
            ["defaults", "write", "-g", "ApplePressAndHoldEnabled", "-bool", "true"],
            check=True,
        )
        typer.echo("✓ Key hold for accents enabled")
        typer.echo("Note: You may need to restart applications")
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error enabling key hold: {e}", err=True)
        raise typer.Exit(1)


@keyboard_app.command()
def repeat():
    """Enable key repeat (disables hold for accents)."""
    try:
        subprocess.run(
            ["defaults", "write", "-g", "ApplePressAndHoldEnabled", "-bool", "false"],
            check=True,
        )
        typer.echo("✓ Key repeat enabled (hold for accents disabled)")
        typer.echo("Note: You may need to restart applications")
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error enabling key repeat: {e}", err=True)
        raise typer.Exit(1)


@keyboard_app.command()
def reset(
    hold: bool = typer.Option(False, "-h", "--hold", help="Reset key hold to default (enabled)"),
    all: bool = typer.Option(False, "-a", "--all", help="Reset all keyboard settings to defaults"),
):
    """Reset keyboard settings. Must specify -h (hold) or -a (all)."""
    if not any([hold, all]):
        typer.echo("Error: Must specify either -h (hold) or -a (all)")
        raise typer.Exit(1)

    try:
        if hold or all:
            # Reset press-and-hold to default (enabled)
            subprocess.run(
                ["defaults", "write", "-g", "ApplePressAndHoldEnabled", "-bool", "true"],
                check=True,
            )
            typer.echo("✓ Key hold reset to default (enabled)")
            
        if all:
            # Add more keyboard settings here as they are implemented
            pass

        typer.echo("Note: You may need to restart applications")
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error resetting keyboard settings: {e}", err=True)
        raise typer.Exit(1)
