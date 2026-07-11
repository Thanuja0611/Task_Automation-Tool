import os
import shutil
from config import FILE_TYPES
from utils import create_folder, get_extension

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Folder not found!")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isdir(file_path):
            continue

        extension = get_extension(filename)
        moved = False

        for folder, extensions in FILE_TYPES.items():
            if extension in extensions:
                destination = os.path.join(folder_path, folder)
                create_folder(destination)
                shutil.move(file_path, os.path.join(destination, filename))
                print(f"Moved: {filename} -> {folder}")
                moved = True
                break

        if not moved:
            destination = os.path.join(folder_path, "Others")
            create_folder(destination)
            shutil.move(file_path, os.path.join(destination, filename))
            print(f"Moved: {filename} -> Others")