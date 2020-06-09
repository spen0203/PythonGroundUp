# Import statements
from datetime import date
from datetime import time
from datetime import datetime

def main():
    # Date Objects

    #Get todays date from the today method
    today = date.today()
    print("todays date is ", today)

    #print date's individual componenets
    print("Date Componenets: " , today.day, today.month, today.year)

    #Retreive todays weekdayNumber ( 0=monday & 6=sunday )
    print("Todays WeekDay # is: " , today.weekday())
    days = ["Mon", "Tues", "Wend", "Thurs", "Fri", "Sat", "Sun"]
    print("which is a: " , days[today.weekday()])



    #DateTime objects
    print("DATETIME OBJECTS: \n\n")

    today = datetime.now()
    print("the current datetime is: ", today)

    # Get the current time
    t = datetime.time(datetime.now())
    print(t)



# It executes the main() function only if this file is executed as the main program.
if __name__ == "__main__":
    main()