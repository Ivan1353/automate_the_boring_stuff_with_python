#This program finds all files with a pdf extension in a directory, copies
#them to a new folder and then creates a zip file from the new folder

import os, shutil, zipfile
path = r"C:\Users\ivand\PycharmProjects\automate\ch_10\files"

folder = input("Please name your Folder: ")
extension = input("Please enter the extension you would like to archive: ")

files = os.listdir(path)
os.chdir(path)
os.makedirs(f".\{folder}")

for file in files:
    if file.endswith(f".{extension}"):
        shutil.copy(file, f".\{folder}")

shutil.make_archive(f"{folder}", 'zip', folder)