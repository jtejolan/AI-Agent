import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        work_dir = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(work_dir, file_path))
        valid_target_file = os.path.commonpath([work_dir, target_file_path]) == work_dir

        ## VALIDATION BLOCK##
        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        ## ACTION BLOCK##
        command = ["python", target_file_path]
        if args is not None:
            command.extend(args)
        
        result = subprocess.run(
            command,
            cwd=work_dir,
            capture_output = True,
            text = True,
            timeout = 30
            
        )
        
        output = ""

        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}\n"

        if result.stdout:
            output += f"STDOUT:\n{result.stdout}\n"

        if result.stderr:
            output += f"STDERR:\n{result.stderr}\n"

        if not result.stdout and not result.stderr:
            output += "No output produced"

        return output


    except Exception as e:
        return f"Error: executing Python file: {e}"