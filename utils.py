import os

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('⚠ Error: Enter a valid number')
    
    
def get_valid_path(prompt):
    while True:
        path = input(prompt).strip().strip('"').strip("'").replace("\\", "/")
        if os.path.exists(path):
            return path
        else:
            print('⚠ Error: Folder does not exist')


def get_all_files(folder_path, video_ext):
    all_files = []
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(video_ext):
                all_files.append(os.path.join(root, file))
    
    all_files.sort()
    return all_files