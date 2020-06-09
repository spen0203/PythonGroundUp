

#Normal class with methods
class myClass():
    def method1(self): #self refers to the class object it is similiar to this in java
        print("myClass method1")

    def method2(self, someString):
        print("myClass method2 " + someString)

#Inheritance 
class anotherClass(myClass): #another class is inheriting myclass
    def method1(self): #self refers to the class object it is similiar to this in java
        myClass.method1(self)
        print("anotherClass method1")

    def method2(self, someString):
        print("anotherClass method2 ")



def main():
    c = myClass() #instantiate object instance
    c.method1()
    c.method2("this is a string")

    c2 = anotherClass()
    c2.method1()
    c2.method2("this is a new string")

if __name__ == "__main__":
    main()