import os

def write_file(working_directory, file_path, content):
    
    
    
    try:
        working_dir_path = os.path.abspath(working_directory)
        target = os.path.normpath(os.path.join(working_dir_path, file_path))        
        valid_target_dir = os.path.commonpath([working_dir_path, target]) == working_dir_path


        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
            
        if os.path.isdir(target):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
            

        parent_dir = os.path.dirname(target)

        os.makedirs( parent_dir, exist_ok=True)

        with open(target, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error: {e}'