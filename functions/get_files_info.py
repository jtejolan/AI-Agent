import os

def get_files_info(working_directory, directory="."):
  work_dir = os.path.abspath(working_directory)
  target_dir = os.path.normpath(os.path.join(work_dir, directory))
  
  os.path.commonpath([work_dir, target_dir])
