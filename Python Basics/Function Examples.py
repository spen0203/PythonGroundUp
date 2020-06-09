



f = 123

#Function that takes wildcard amount of variables
# * means it can be any amount 
def add_Multiple(*args):
    result = 0
    for x in args: #set x = to each item in the args list
        result = result + x
    return result



# Function that sets a default value to x incase its not passed
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#basic pass params
def multiply(arg1 , arg2):
    return arg1 * arg2


#Basic main function
def main():
    print("hello world")
    f = "abc"
    print(f) 


# This if statement checks where the files called from
# if it is launched from a terminal or exe it is considered true and will run main
#
# otherwise it is assumed another file or program has called it to use internal functions 
# without the need use main (it works as an extension or standalone)
if __name__ == "__main__":
    main()
    print(f)

    del f # deletes previous declaration of f

    multiply(1,2)#pass params

    #power function (default param value example)
    print("Power default param examples")
    print(power(2))
    print(power(2,3))
    print(power(x=3, num =1)) #Python allows you to use params in any order if you include var names with the value

    #wildcard args
    print("wildcard number of params examples")
    print(add_Multiple(10,20,30))
    print(add_Multiple())
    print(add_Multiple(10))

