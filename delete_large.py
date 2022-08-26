#This program allows you to delete files above a particular size from a file directory

import os
import send2trash

path = input("Please enter the path of the directory where files will be deleted:")
size = int(input("Please enter the size above which you would like files to be deleted:"))

for folderName, subfolders, filenames in os.walk(path):
    for file in filenames:
        fileSize=os.path.getsize(file)
        if fileSize >= 100000:
            send2trash.send2trash(file)