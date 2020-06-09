import calendar #import calandar module

def main():
    #Create a plain console txt calandar
    c = calendar.TextCalendar(calendar.SUNDAY) # initialize new calandar that starts on sunday
    st = c.formatmonth(2017, 1, 0, 0) #Jan 2017
    print(st) #Prints out calandar of Jan 2017

    #loop over days of month
    for i in c.itermonthdates(2017,8): # august 2017 
        if(i != 0): # if the week includes a day from another month it will display 0
            print(i) # Prints out each day ie 1, 2, 3 ... 30


    # User Locale print months & day in local format
    for name in calendar.month_name:
        print(name)
    for day in calendar.day_name:
        print(day)

    # Calculate days based on a rule
    #ie team meeting on the first friday of each month

    print("Team meetings will be on: ")
    for m in range(1,13): # Goes through each month 1-12 
        cal = calendar.monthcalendar(2018, m) # create an array of the current month
        weekOne = cal[0] # Get the first week of the month
        weekTwo = cal[2]

        if weekOne[calendar.FRIDAY] != 0: #if the friday value of week one is 0 its a different month
            meetday = weekOne[calendar.FRIDAY]
        else:
            meetday = weekTwo[calendar.FRIDAY]

        print("%10s %2d" % (calendar.month_name[m], meetday))#Prints out the month name and date value ie: January 5 \n February 2 \n ...




    #Create a HTML formatted Calandar
    #Puts it into html with custom classes for each day ie class="sun"
    hc = calendar.HTMLCalendar(calendar.SUNDAY)
    st = hc.formatmonth(2017, 1)
    print(st)



if __name__ == "__main__":
    main()