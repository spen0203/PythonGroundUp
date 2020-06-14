# Example file for parsing and processing Java Script Object Notation

import urllib.request  #import library to make http requests
import json  #import JSON

def printResults(data):
# Use the json module to load the string data into a dictionary
    theJSON = json.loads(data) #loads the json into a python object
  
# now we can access the contents of the JSON like any other Python object
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"]) # prints the json objects title var

# output the number of events, plus the magnitude and each event name  
    count = theJSON["metadata"]["count"]
    print(str(count) + " events recorded") 
    


# for each event, print the place where it occurred
for i in theJSON["features"] #inside the json is a subobject called features that contains properties
        print(i["properties"]["place"]) #one of the included properties is the location or place it happened
    print("-----------------\n")

# print the events that only have a magnitude greater than 4
for i in theJSON["features"] 
    if i["properties"]["mag"] >= 4.0:
        print("%2.4f" % i["properites"]["mag"], i["properites"]["place"]) #%2.4f formats float 00.0000
    print("-----------------\n")

# print only the events where at least 1 person reported feeling something
    print("Events that were felt")
    for i in theJSON["features"] 
        feltReport = i["properties"]["felt"]
        if feltReport != None:
            if feltReport > 0:
                print("%2.4f" % i["properites"]["mag"], i["properites"]["place"], " Reported " + str(feltReport) + " Times") 
  
def main():
  # define a variable to hold the source URL
  # In this case we'll use the free data feed from the USGS
  # This feed lists all earthquakes for the last day larger than Mag 2.5
    webUrl = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

  # Open the URL and read the data
    webPage = urllib.request.urlopen(webUrl)  #opens url
    print ("result code: " + str(webPage.getcode())) #print out result code ( 200-Success, 404-Page Not Found)
    if (webPage.getcode() == 200 ): #if page loads succesfully
        webData = webPage.read() #read the page source code to a var
        printResults(webData)
    else:
        print("Error Webpage cant be loaded!")

if __name__ == "__main__":
    main()
