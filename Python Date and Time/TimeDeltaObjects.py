# Import statements
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta #timedeltas are a span of time


def main():
    print(timedelta(days=365, hours=5, minutes=1))

    now = datetime.now()
    print("Today is: ", str(now))

    #Future Dates
    #One year away
    print("One year from now will be: " + str(now + timedelta(days=365)))
    #Using more than one argument
    print("In two days and 3 weeks it will be: " + str(now + timedelta(days=2 , weeks =3)))

    #Past Dates
    t = datetime.now() - timedelta(weeks=1)
    s = t.strftime("%A %B %d, %Y")
    print("One week ago it was: " + s)



    #How many days till April Fools (April 1st)
    today = date.today()
    afd = date(today.year, 4 , 1) #Uses todays year

    if (afd < today):
        print("april fools already happened %d days ago" % ((today-afd).days))
        afd = afd.replace(year = today.year+1) #Replace the afd date with next year
    
    time_to_afd = afd - today
    print("It is ", time_to_afd.days , " days until April Fools day")


# It executes the main() function only if this file is executed as the main program.
if __name__ == "__main__":
    main()