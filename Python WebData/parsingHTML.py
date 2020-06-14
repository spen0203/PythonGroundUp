#Example file for parsing and proccessing HTML
from html.parser import HTMLParser

metaCount = 0

class myHTMLParser(HTMLParser):
    def handle_comment(self, data): #Searches for <!-- --> 
        print("encountered comment: ", data)
        pos = self.getpos() #Get position of comment
        print("\t at line: ", pos[0], " position ", pos[1])


    def handle_starttag(self, tag, attrs): #start tag is called at the end of a tag ie <title> ">" is where its called
        global metaCount
        if tag == "meta":
            metaCount += 1
        print("encountered startTag: ", tag)
        pos = self.getpos() #Get position of comment
        print("\t at line: ", pos[0], " position ", pos[1])
        #check for attributes
        if attrs.__len__() > 0: #check that theres itleast one atribute
            print("\t attributes:")
            for a in attrs:
                print("\t", a[0] , " = ", a[1]) #attribute name followed by value



    def handle_endtag(self, tag):
        print("encountered endTag: ", tag)
        pos = self.getpos() #Get position of end tag
        print("\t at line: ", pos[0], " position ", pos[1])

    def handle_data(self, data):
        if(data.isspace()): #ensure the data isnt white space
            return
        print("encountered data: ", data)
        pos = self.getpos() #Get position of comment
        print("\t at line: ", pos[0], " position ", pos[1])


def main():
    #instantiate the parser class
    parser = myHTMLParser()
    f = open("samplehtml.html") #open local html file
    if f.mode == 'r': #confirm it opened
        contents = f.read() 
        parser.feed(contents)
    print("MetaTags found: " + str(metaCount))



if __name__ == "__main__":
    main()