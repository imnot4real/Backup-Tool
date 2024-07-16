import os
import shutil
import argparse
from datetime import datetime

def create_backup(source, destination):
    # Create a timestamp for the backup folder
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = os.path.join(destination, f"backup_{timestamp}")

    try:
        # Create the backup directory
        os.makedirs(backup_dir)

        # Copy the source to the backup directory
        if os.path.isfile(source):
            shutil.copy2(source, backup_dir)
        elif os.path.isdir(source):
            shutil.copytree(source, os.path.join(backup_dir, os.path.basename(source)))
        
        print(f"Backup created successfully at: {backup_dir}")
    except Exception as e:
        print(f"An error occurred during backup: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Backup Tool: A simple utility to back up files and directories.")
    parser.add_argument("source", help="Source file or directory to backup")
    parser.add_argument("destination", help="Destination directory for the backup")

    args = parser.parse_args()

    if not os.path.exists(args.source):
        print(f"Error: Source '{args.source}' does not exist.")
        return

    if not os.path.isdir(args.destination):
        print(f"Error: Destination '{args.destination}' is not a valid directory.")
        return

    create_backup(args.source, args.destination)

if __name__ == "__main__":
    main()