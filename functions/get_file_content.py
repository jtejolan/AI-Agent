import os
from config import *
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        work_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(work_dir, file_path))
        valid_target_file = os.path.commonpath([work_dir, target_file]) == work_dir

        # VALIDATION BLOCK
        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        elif not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_file, "r") as file:
            content = file.read(MAX_CHARS)
            if file.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]' 

        return content

    except Exception as e:
        return f"Error: {e}"

##Schema##    

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a file in a specified working directory up to 10000 characters.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to file that needs to be read, relative to the working directory",
            ),
        
        },
        required=["file_path"]
    ),  
)