from pathlib import Path
import shutil


def mode_selection() -> str:
    mode_dict = {1: "default: extensions", 2: "selective: category"}
    print(mode_dict)
    try:
        selected_mode: str = mode_dict.get(int(input("mode: ")), "default: extensions")
    except ValueError:
        selected_mode = "default: extensions"
    return selected_mode


def organize_extentions(target_folder):
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


def organize_category(target_folder, custom_mapping):
    path = Path(target_folder)

    if not path.exists():
        print(f"Error: The path '{target_folder}' does not exist.")
        return

    # Create a quick-lookup map: extension -> category name
    # e.g., {'jpg': 'Images', 'png': 'Images', 'pdf': 'Documents', ...}
    ext_to_category = {}
    for category, extensions in custom_mapping.items():
        for ext in extensions:
            ext_to_category[ext.lower().lstrip(".")] = category

    # Iterate through items in the target directory
    for item in path.iterdir():
        if item.is_file():
            file_ext = item.suffix[1:].lower()

            if not file_ext:
                continue  # Skip files without extensions

            # Look up the category. If the extension isn't in our mapping,
            # fall back to using the extension name itself (e.g., 'exe' -> 'exe')
            folder_name = ext_to_category.get(file_ext, file_ext)

            # Create the category folder if it doesn't exist
            category_folder = path / folder_name
            category_folder.mkdir(exist_ok=True)

            # Move the file into the category folder
            destination = category_folder / item.name
            shutil.move(str(item), str(destination))
            print(f"Moved: {item.name} -> {folder_name}/")

    print("✨ Category-based folder organization complete!")


mode = mode_selection()
if mode == "default: extensions":
    organize_extentions(input("folder_path: "))

elif mode == "selective: category":
    CATEGORY_MAPPING = {
        "Images": ["jpg", "jpeg", "png", "gif", "webp", "svg"],
        "Documents": ["pdf", "docx", "doc", "txt", "xlsx", "csv", "pptx"],
        "Archives": ["zip", "tar", "gz", "rar", "7z"],
        "Media": ["mp4", "mkv", "mp3", "wav", "flac"],
        "Code": ["py", "js", "html", "css", "json"],
    }
    organize_category(input("folder_path: "), CATEGORY_MAPPING)
