# Automation Project — File Backup Tool

from pathlib import Path

import shutil

path = Path(input("Enter the folder you want to backup: "))

if path.exists():

    name = "Backup_" + path.name

    backup_location = Path(
        input("Enter the path where you want to create the backup: ")
    )

    folder = backup_location / name

    folder.mkdir(parents=True, exist_ok=True)

    for item in path.rglob("*"):

        if item.is_file():

            relative_path = item.relative_to(path)

            destination = folder / relative_path

            destination.parent.mkdir(parents=True, exist_ok=True)

            shutil.copy2(item, destination)

            print(f"Copied: {item.name}")

    print(f"\nBackup completed successfully!")

    print(f"Backup location: {folder}")

else:
    print("The folder does not exist.")