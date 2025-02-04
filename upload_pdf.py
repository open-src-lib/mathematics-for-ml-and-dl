import subprocess
from pathlib import Path


def main():
    root_dir = Path.cwd()
    local_dir = root_dir / "data"
    remote_dir = f"open-src-lib:/{root_dir.parts[-1]}"

    command = ["rclone", "sync", local_dir, remote_dir, "--progress"]
    try:
        subprocess.run(command, check=True)
        print("Synced successfully")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
