import os
from os import path
import datetime
from datetime import date,time,timedelta
import time

def main():
    # Print the name of the OS
    print(os.name)

    #Check for item existance and its type ( booleans )
    print("Item exists: " + str(path.exists("textfile.txt"))) 
    print("Item is a file: " + str(path.isfile("textfile.txt"))) 
    print("Item is directory: " + str(path.isdir("textfile.txt"))) 

    #Get file path
    print("Item Path: " + str(path.realpath("textfile.txt")))
    print("Item Path and name : " + str(path.split(path.realpath("textfile.txt")))) 

    #File modification Time
    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))) #alt format


    #Calculate time since last modication
    td = datetime.datetime.now() -datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("it has been "+ str(td) +" since the file was modified")
    print("OR, " + str)(td.total_seconds()) + " seconds")

    


if __name__ == "__main__":
    main()