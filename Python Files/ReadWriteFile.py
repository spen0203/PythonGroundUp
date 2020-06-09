
def main():
    #Open a file for writing, or create if it doesnt exist
    f = open("textfile.txt", "w+") #(filename, file permissions) | + allows the system to create file if it doesnt exist

    #Write data to the file
    for i in range(10):
        f.write("this is line " + str(i) + "\r\n")

    #close file when done
    f.close()


    #Append text to the end of file
    f = open("textfile.txt", "a") 
    for i in range(10):
        f.write("this is an append line " + str(i) + "\r\n")
    f.close()

    #Read File

    #Read entire file
    f = open("textfile.txt", "r") 
    if f.mode == 'r': #Confirm file is succesfully opened
        contents = f.read()
        print(contents)
    f.close()

    #Read Line by Line
    f = open("textfile.txt", "r") 
    if f.mode == 'r': 
        fl = f.readlines()
        for x in fl:
            print(x)
        f.close()
   

if __name__ == "__main__":
    main()