import os

def update_home_html(directory_path):
    home_html_path = os.path.join(directory_path, 'home.html')
    
    # Read the content of home.html
    try:
        with open(home_html_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"File '{home_html_path}' not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    # Use a set to keep track of already processed folder names
    processed_folders = set()

    # List all directories in the given directory path
    try:
        for folder_name in os.listdir(directory_path):
            folder_path = os.path.join(directory_path, folder_name)
            
            # Check if it is a directory
            if os.path.isdir(folder_path):
                # Check if the folder name is already present in the file content
                if folder_name not in processed_folders and folder_name not in content:
                    # Replace the first occurrence of 'Outlet 2' with the folder name in the file content
                    if 'Outlet 2' in content:
                        new_content = content.replace('Outlet 2', folder_name, 1)
                        content = new_content
                        processed_folders.add(folder_name)
                        print(f"Updated 'Outlet 2' to '{folder_name}' in '{home_html_path}'")
                else:
                    print(f"Folder name '{folder_name}' is already present in the file or has been processed.")
    except Exception as e:
        print(f"An error occurred while processing directories: {e}")
        return

    # Write the updated content back to the home.html file
    try:
        with open(home_html_path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

# Replace 'path/to/sfs' with the actual path to the 'sfs' directory
sfs_directory_path = 'C:/Users/nakir/Downloads/sfs-20240520T110909Z-001/sfs'
update_home_html(sfs_directory_path)