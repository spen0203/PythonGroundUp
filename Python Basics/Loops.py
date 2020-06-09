
def main():
    x = 0


    #basic while loop
    while (x < 5):
        print(x)
        x = x + 1

    #basic for loop uses a range
    # starts at first param stops < second param
    for x in range (5, 10):
        print(x)

    #For loop over a collection
    days = ["Mon", "Tues", "Wend", "Thurs", "Fri", "Sat", "Sun"]
    for d in days:
        print(d)
    
    #Break statement
    for x in range(5,10):
        if(x == 7): break  #upon reaching 7 it breaks from loop
        print(x)
    #Continue Statement
    for x in range(5,10):
        if( x % 2 == 0): continue # if modulus 2 = 0 continue from the next value in the loop(wont print 6 || 8)
        print(x)

    # enumerate() Function to get index
    days = ["Mon", "Tues", "Wend", "Thurs", "Fri", "Sat", "Sun"]
    for i,d in enumerate(days): # Returns the index and Value
        print(i, d)




# It executes the main() function only if this file is executed as the main program.
if __name__ == "__main__":
    main()