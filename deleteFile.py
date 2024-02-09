import os

def deleteFilesInFolder(folder_path, file_extensions=None):
    try:
        if file_extensions is None:
            file_extensions = []

        deleted_count = 0

        # Perform delete and log in console
        for file_name in os.listdir(folder_path):
            if not file_extensions or any(file_name.lower().endswith(ext) for ext in file_extensions):
                file_path = os.path.join(folder_path, file_name)
                os.remove(file_path)
                print(f"Deleted: {file_path}")
                deleted_count += 1

        print(f"Deleted {deleted_count} files in '{folder_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Path to the folder containing the files to be deleted
folder_to_clean = "path/to/folder/"

# File extensions to be deleted
file_extensions_to_delete = ['.jpg', '.png', '.jpeg']

deleteFilesInFolder(folder_to_clean, file_extensions_to_delete)