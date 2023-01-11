#rename_files.py is a tool for organizing large collections of files.
#Upon being provided the file path to a root folder, files are renamed
#"[folder name]_x.[extention]" with x being an incrementing digit.
#Folder names are not changed. -Garrett 2023

import os, time

def renameFiles(path, folder_name):
    sleepPrint(f"Renaming contents of {folder_name}")
    for count, filename in enumerate(os.listdir(f"{path}{folder_name}")):
        file_extention = filename[filename.rindex("."):]
        new_name = f"{folder_name}_{str(count)}{file_extention}"
        source_file = f"{path}{folder_name}/{filename}"
        final_name = f"{path}{folder_name}/{new_name}"
        os.rename(source_file, final_name)
    sleepPrint("Done!", last=True)

def sleepPrint(msg, last=False):
    if (last == False):
        print(msg, end="")
        for i in range(3):
            print(".", end="")
        print()
    else:
        for i in range(3):
            print(".", end="")
        print(msg)

def getPath():
    input_path = input('Provide a folder path to rename it\'s contents: ')
    x = input_path.rindex("\\")+1
    path = input_path[:x]
    folder = input_path[x:]
    return (path, folder)

def begin():
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~')
    target_folder = getPath() 
    renameFiles(target_folder[0], target_folder[1])

#~~~~~~~~~~~~~~~~~~ MAIN ~~~~~~~~~~~~~~~~~~#

begin()
