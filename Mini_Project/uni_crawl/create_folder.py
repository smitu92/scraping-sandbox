import os
import re  # for filename sanitization

def verify_folder_exists(folder_name):
    if os.path.exists(folder_name):
        print(f"Folder '{folder_name}' already exists.")
        return True
    return False

def create_subfolder(parent_folder, subfolder_name):
    # Sanitize subfolder name to remove invalid characters
    sanitized_subfolder_name = re.sub(r'[<>:"/\\|?*]', '_', subfolder_name)
    
    # Create the subfolder path
    subfolder_path = os.path.join(parent_folder, sanitized_subfolder_name)
    
    # Create the subfolder if it doesn't exist
    verify_folder_exists(subfolder_path) or os.makedirs(subfolder_path)

def create_folder(folder_name):
    # Sanitize folder name to remove invalid characters
    sanitized_name = re.sub(r'[<>:"/\\|?*]', '_', folder_name)
    
    # Create the folder if it doesn't exist
    verify_folder_exists(sanitized_name) or os.makedirs(sanitized_name)
    # create_subfolder(sanitized_name, "Semester 1")
    # create_subfolder(sanitized_name, "Semester 2")


# create_folder("Exam Papers")

