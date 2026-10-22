from pathlib import Path
import shutil


def organize_folder(target_folder):
    path = Path(target_folder)

    # Check if the folder exists
    if not path.exists():
        print(f"Error: The path '{target_folder}' does not exist.")
        return

    # Iterate through all items in the directory
    for item in path.iterdir():
        # Process only files (ignore subdirectories)
        if item.is_file():
            # Get the file extension (e.g., '.pdf' becomes 'pdf')
            file_extension = item.suffix[1:].lower()

            if not file_extension:
                continue  # Skip files without extensions

            # Create a folder for this extension if it doesn't already exist
            ext_folder = path / file_extension
            ext_folder.mkdir(exist_ok=True)

            # Move the file into the extension folder
            destination = ext_folder / item.name
            shutil.move(str(item), str(destination))
            print(f"Moved: {item.name} -> {file_extension}/")

    print("Folder organization complete!")


organize_folder(input("folder_path: "))
