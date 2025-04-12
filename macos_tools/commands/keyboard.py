import typer
import subprocess

keyboard_app = typer.Typer()


@keyboard_app.command()
def disable_accent_hold():
    """Disable the press-and-hold feature for accented characters."""
    try:
        # Disable press-and-hold for accented characters
        subprocess.run(
            [
                "defaults",
                "write",
                "-g",
                "ApplePressAndHoldEnabled",
                "-bool",
                "false",
            ],
            check=True,
        )
        print("✅ Press-and-hold for accented characters has been disabled.")
        print(
            "Note: You may need to restart your applications for changes to take effect."
        )
    except subprocess.CalledProcessError as e:
        print(f"❌ Error disabling press-and-hold: {e}")
        raise typer.Exit(1)


@keyboard_app.command()
def enable_accent_hold():
    """Enable the press-and-hold feature for accented characters."""
    try:
        # Enable press-and-hold for accented characters
        subprocess.run(
            [
                "defaults",
                "write",
                "-g",
                "ApplePressAndHoldEnabled",
                "-bool",
                "true",
            ],
            check=True,
        )
        print("✅ Press-and-hold for accented characters has been enabled.")
        print(
            "Note: You may need to restart your applications for changes to take effect."
        )
    except subprocess.CalledProcessError as e:
        print(f"❌ Error enabling press-and-hold: {e}")
        raise typer.Exit(1)
