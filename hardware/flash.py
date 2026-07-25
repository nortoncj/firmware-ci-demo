import subprocess

subprocess.run([
    "pio",
    "run",
    "--target",
    "upload"
], check=True)