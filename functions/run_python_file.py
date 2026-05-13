import os
from config import *

def run_python_file(working_directory, file_path, args=None):
    try:
        work_dir = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(work_dir, file_path))
        valid_target_file = os.path.commonpath([work_dir, target_file_path]) == work_dir

        # VALIDATION BLOCK
        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", absolute_file_path]
        

    except Exception as e:
        return f"Error: {e}"