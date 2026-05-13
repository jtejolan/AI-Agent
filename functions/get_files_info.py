import os

def get_files_info(working_directory, directory="."):
    try:
        work_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(work_dir, directory))
        valid_target_dir = os.path.commonpath([work_dir, target_dir]) == work_dir

        # VALIDATION BLOCK
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        elif not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        dir_items = os.listdir(target_dir)

        string = ""

        for item in dir_items:
            path = os.path.join(target_dir, item)
            name = item
            file_size = os.path.getsize(path)
            is_dir = os.path.isdir(path)

            string += f"- {name}: file_size={file_size} bytes, is_dir={is_dir}\n"

        return string
    except Exception as e:
        return f"Error: {e}"
    

