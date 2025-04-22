import subprocess
import typer

system_app = typer.Typer()


@system_app.command(name="enable-touchid-sudo")
def enable_touchid_sudo():
    """Enable Touch ID authentication for sudo commands."""
    try:
        # Check if the line already exists
        result = subprocess.run(
            ["grep", "auth sufficient pam_tid.so", "/etc/pam.d/sudo"],
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            typer.echo("Touch ID for sudo is already enabled")
            return

        # Create a backup of the original file
        subprocess.run(
            ["sudo", "cp", "/etc/pam.d/sudo", "/etc/pam.d/sudo.bak"],
            check=True,
        )

        # Add the line at the top of the sudo PAM file using a temporary file
        subprocess.run(
            [
                "sudo",
                "sh",
                "-c",
                'echo "auth sufficient pam_tid.so" | cat - /etc/pam.d/sudo > /tmp/sudo.pam && sudo mv /tmp/sudo.pam /etc/pam.d/sudo',
            ],
            check=True,
        )
        typer.echo("✓ Touch ID for sudo has been enabled")
        typer.echo("✓ Original file backed up as /etc/pam.d/sudo.bak")

    except subprocess.CalledProcessError as e:
        typer.echo(f"Error enabling Touch ID for sudo: {e}", err=True)
        raise typer.Exit(1)
