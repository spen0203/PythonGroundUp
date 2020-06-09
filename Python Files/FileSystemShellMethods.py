import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    #Duplicate an existing file
    if path.exists("textfile.txt"): # Confirm the file exists
        #Get the full path to the file
        src = path.realpath("textfile.txt")

        
        #Create a backup by appending .bak to the name
        dst = src +".bak"


        #Copy the file
        shutil.copy(src,dst) #Contents
        shutil.copystat #Copy the file contents and permissions, modification info


        #rename the original file
        os.rename("textfile.txt", "newfile.txt") #renames the first file param to be the second name


        #Zip the entire Directory ie Python Files
        root_dir, tail = path.split(src)
        shutil.make_archive("archive", "zip", root_dir ) #(name, type, directoryToBeZipped)


        #Zip Specific items
        with ZipFile("testZip.zip", "w") as newzip: #Create a new zip  and use newzip as a scope object to modify it
            newzip.write("textfile.txt")
            newzip.write("textfile.txt.bak")


if __name__ == "__main__":
    main()