import os

def getPath():
    return input('Provide a folder path to review it\'s contents: ')

def printDir(path):
    dirs = os.listdir(path)
    for file in dirs:
        print(file)
        if (file.find(".")<0):
            print(f"Opening \"{file}\"...")
            printDir(f"{path}/{file}")

def breakPath(path):
    x = path.rindex("\\")+1
    path_root = path[:x]
    root_folder = path[x:]
    return (path_root, root_folder)

def begin():
    target_path = getPath()
    target_roots = breakPath(target_path)
    print(f"Showing contents of {target_roots[-1]}...")
    printDir(target_path)

#~~~~~~~~~~~~~~~~~~~~ MAIN ~~~~~~~~~~~~~~~~~~~~

begin()
