#rename_files_folder_drill.py is a tool for organizing large collections of 
#files. Upon being provided the file path to a root folder, folder_drill.py
#drills into that directory. Files are renamed "[folder name]_x.[extention]"
#with x being an incrementing digit. Folder names are not changed.-Garrett 2023

import os

def renameFiles(path, folder_name):
    print(f"Renaming contents of {folder_name}")
    for count, filename in enumerate(os.listdir(f"{path}{folder_name}")):
        if (filename.find(".")<0):
            print(f"Opening \"{filename}\"...")
            drill_path = f"{path}{folder_name}/"
            renameFiles(drill_path, filename)
        else:    
            file_extention = filename[filename.rindex("."):]
            new_name = f"{folder_name}_{str(count)}{file_extention}"
            source_file = f"{path}{folder_name}/{filename}"
            final_name = f"{path}{folder_name}/{new_name}"
            os.rename(source_file, final_name)
            print(f"Renamed {filename} to {new_name}")

def getPath():
    return input('Provide a folder path to rename it\'s contents: ')
 
def breakPath(path):
    x = path.rindex("\\")+1
    path_root = path[:x]
    root_folder = path[x:]
    return (path_root, root_folder)

def begin():
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~')
    target_path = getPath()
    target_roots = breakPath(target_path)
    renameFiles(target_roots[0], target_roots[1])

#~~~~~~~~~~~~~~~~~~ MAIN ~~~~~~~~~~~~~~~~~~#

begin()
