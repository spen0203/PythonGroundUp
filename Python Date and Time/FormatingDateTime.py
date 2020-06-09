from datetime import datetime



def main():
    now = datetime.now()

    #DATE FORMATING

    # %y %Y - year , %a %A - Weekday, %b %B - month, %d day of month 
    print(now.strftime("The current year is: %Y"))
    print(now.strftime("%a, %d %B, %y"))

    #Locale specific information
    print(now.strftime("Locale date & time: %c "))
    print(now.strftime("Locale date: %x "))
    print(now.strftime("Locale time: %X "))


    #Time Formatting
    # %I/%H - 12/24H , %M minute, %s Second, %p Locales AM/PM
    print(now.strftime("The current Time is: %I:%M:%S %p"))
    print(now.strftime("24 Hour Time is: %H:%M"))


# It executes the main() function only if this file is executed as the main program.
if __name__ == "__main__":
    main() 