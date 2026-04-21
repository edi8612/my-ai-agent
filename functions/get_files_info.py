import os


def get_files_info(working_directory, directory="."):
    try:
        working_dir_path = os.path.abspath(working_directory)
        target = os.path.normpath(os.path.join(working_dir_path, directory))
        
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_path, target]) == working_dir_path

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target):
            return f'Error: "{directory}" is not a directory'

        lines = []
        items = os.listdir(target)
        for item in items:
            item_path = os.path.join(target, item)
            size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            lines.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {e}"    
    