import subprocess
import typer

dock_app = typer.Typer()

@dock_app.command(name="size")
def set_size(
    size: int = typer.Argument(None, help="Size of dock icons (32-128)")
):
    """Set the size of dock icons."""
    if size is None:
        # Show current size when no argument is provided
        try:
            result = subprocess.run(
                ["defaults", "read", "com.apple.dock", "tilesize"],
                capture_output=True,
                text=True,
                check=True,
            )
            current_size = int(result.stdout.strip())
            typer.echo(f"Current dock size: {current_size}")
            return
        except subprocess.CalledProcessError:
            typer.echo("Could not read current dock size")
            return

    if not (32 <= size <= 128):
        typer.echo("Size must be between 32 and 128")
        raise typer.Exit(1)

    try:
        subprocess.run(
            ["defaults", "write", "com.apple.dock", "tilesize", "-integer", str(size)],
            check=True,
        )
        subprocess.run(["killall", "Dock"], check=True)
        typer.echo(f"Dock size set to {size}")
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error setting dock size: {e}", err=True)


@dock_app.command()
def reset(
    size: bool = typer.Option(False, "-s", "--size", help="Reset dock size to default (64)"),
    hide: bool = typer.Option(False, "-h", "--hide", help="Reset dock auto-hide to default (disabled)"),
    lock: bool = typer.Option(False, "-l", "--lock", help="Reset dock size lock to default (unlocked)"),
    all: bool = typer.Option(False, "-a", "--all", help="Reset all dock settings to defaults"),
):
    """Reset dock settings. Must specify one or more flags: -s (size), -h (hide), -l (lock), or -a (all)."""
    if not any([size, hide, lock, all]):
        typer.echo("Error: Must specify at least one flag: -s (size), -h (hide), -l (lock), or -a (all)")
        raise typer.Exit(1)

    try:
        if size and not all:
            # Reset only the size to default (64)
            subprocess.run(
                ["defaults", "write", "com.apple.dock", "tilesize", "-integer", "64"],
                check=True,
            )
            subprocess.run(["killall", "Dock"], check=True)
            typer.echo("✓ Dock size reset to default (64)")

        if hide and not all:
            # Reset only the autohide setting
            subprocess.run(
                ["defaults", "write", "com.apple.dock", "autohide", "-bool", "false"],
                check=True,
            )
            subprocess.run(["killall", "Dock"], check=True)
            typer.echo("✓ Dock auto-hide reset to default (disabled)")

        if lock and not all:
            # Reset only the size lock setting
            subprocess.run(
                ["defaults", "write", "com.apple.dock", "size-immutable", "-bool", "false"],
                check=True,
            )
            subprocess.run(["killall", "Dock"], check=True)
            typer.echo("✓ Dock size lock reset to default (unlocked)")

        if all:
            # Reset all settings
            subprocess.run(
                ["defaults", "write", "com.apple.dock", "tilesize", "-integer", "64"],
                check=True,
            )
            
            subprocess.run(
                ["defaults", "write", "com.apple.dock", "autohide", "-bool", "false"],
                check=True,
            )
            
            subprocess.run(
                ["defaults", "write", "com.apple.dock", "size-immutable", "-bool", "false"],
                check=True,
            )
            
            subprocess.run(["killall", "Dock"], check=True)
            typer.echo("✓ All dock settings reset to defaults")

    except subprocess.CalledProcessError as e:
        typer.echo(f"Error resetting dock: {e}", err=True)
        raise typer.Exit(1)


@dock_app.command()
def lock():
    """Lock the dock size."""
    try:
        subprocess.run(
            ["defaults", "write", "com.apple.dock", "size-immutable", "-bool", "true"],
            check=True,
        )
        subprocess.run(["killall", "Dock"], check=True)
        typer.echo("Dock size locked")
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error locking dock: {e}", err=True)


@dock_app.command()
def unlock():
    """Unlock the dock size."""
    try:
        subprocess.run(
            ["defaults", "write", "com.apple.dock", "size-immutable", "-bool", "false"],
            check=True,
        )
        subprocess.run(["killall", "Dock"], check=True)
        typer.echo("Dock size unlocked")
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error unlocking dock: {e}", err=True)


@dock_app.command()
def hide():
    """Hide the dock automatically when unused."""
    try:
        subprocess.run(
            ["defaults", "write", "com.apple.dock", "autohide", "-bool", "true"],
            check=True,
        )
        subprocess.run(["killall", "Dock"], check=True)
        typer.echo("Dock will now auto-hide")
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error enabling dock auto-hide: {e}", err=True)


@dock_app.command()
def show():
    """Keep the dock always visible."""
    try:
        subprocess.run(
            ["defaults", "write", "com.apple.dock", "autohide", "-bool", "false"],
            check=True,
        )
        subprocess.run(["killall", "Dock"], check=True)
        typer.echo("Dock will stay visible")
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error disabling dock auto-hide: {e}", err=True)
