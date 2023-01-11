#rename_files_folder_drill.py is a tool for organizing large collections of 
#files. Upon being provided the file path to a root folder, folder_drill.py
#drills into that directory. Files are renamed "[folder name]_x.[extention]"
#with x being an incrementing digit. Folder names are not changed.-Garrett 2023

import os

def drill(path, folder_name):
    print(f"Renaming contents of {folder_name}")
    for count, filename in enumerate(os.listdir(f"{path}{folder_name}")):
        if (filename.find(".")<0):
            print(f"Opening \"{filename}\"...")
            drill_path = f"{path}{folder_name}/"
            drill(drill_path, filename)
        else:   
            renameFile(path, folder_name, count, filename)
            
def renameFile(path, folder_name, count, filename):
    names = buildFileNames(path, folder_name, count, filename)
    os.rename(names[1],names[2])

def buildFileNames(path, folder_name, count, filename):
    file_extention = filename[filename.rindex("."):]
    new_name = f"{folder_name}_{str(count)}{file_extention}"
    source_file = f"{path}{folder_name}/{filename}"
    final_name = f"{path}{folder_name}/{new_name}"
    if os.path.exists(final_name) or filename==new_name:
        new_name = f"{folder_name}_0{str(count)}{file_extention}"
        source_file = f"{path}{folder_name}/{filename}"
        final_name = f"{path}{folder_name}/{new_name}"
    return (new_name,source_file,final_name)

def getPath():
    msg = "\n~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    msg = f"{msg}Provide a folder path to rename it\'s contents: "
    path = input(f"{msg}")
    x = path.rindex("\\")+1
    path_root = path[:x]
    root_folder = path[x:]
    return (path_root, root_folder)

def begin():
    target_roots = getPath()
    drill(target_roots[0], target_roots[1])

#~~~~~~~~~~~~~~~~~~ MAIN ~~~~~~~~~~~~~~~~~~#

begin()
