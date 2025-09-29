import os

def get_files_info(working_directory, directory="."):

# Build   
    allowed_root = os.path.abspath(working_directory)
    print(f"working directory = {allowed_root}\n")

    target = os.path.abspath(os.path.join(working_directory, directory))
    print(f"directory = {target}")

#Check
    if not target.startswith(allowed_root):
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    
    if not os.path.isdir(target):
        return (f'Error: "{directory}" is not a directory')
    
#Loop

    files_info = ""
    for item in os.listdir(target):
        entry = os.path.join(target, item)
        size = os.path.getsize(entry)
        is_dir = os.path.isdir(entry)

        files_info += f"- {item}: file_size={size} bytes, is_dir={is_dir}\n"
        

    return(files_info)