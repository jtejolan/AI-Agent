import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        work_dir = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(work_dir, file_path))
        valid_target_file = os.path.commonpath([work_dir, target_file_path]) == work_dir

        if not valid_target_file:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        parent_directory = os.path.dirname(target_file_path)
        os.makedirs(parent_directory, exist_ok=True)

        with open(target_file_path, "w") as file:
            written_file = file.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites a file at specified path",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to file to be written to relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Text to be written in the specified file",
            ),
        },
        required=["file_path", "content"],
    ),
)