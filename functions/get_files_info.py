import os

def get_files_info(working_directory, directory="."):
    try:
        work_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(work_dir, directory))
        valid_target_dir = os.path.commonpath([work_dir, target_dir]) == work_dir

        if not valid_target_dir:
                return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        elif not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        else:
            return f'Success: "{directory}" is within the working directory'
        
    except Exception as e:
        return f"Error: {e}"
