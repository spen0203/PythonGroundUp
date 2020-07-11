from selenium import webdriver
import os

#############################################
## Parsing HTML DOM Structure Using Selenium:
# The first matching item is always returned.
#############################################


# Find Element Based on id tag
def parse_by_id(driver):
    login_form = driver.find_element_by_id('loginForm') #find element by ID
    print("My login form element is:")
    print(login_form)
    driver.close()
    #My login form element is:
    #<selenium.webdriver.remote.webelement.WebElement (session="d022c55ffb135a8984c4fa2c23be173f", element="0559f28b-d505-4caf-9186-1943c6948211")>


# Find Element Based on name tag
def parse_by_name(driver):
    username = driver.find_element_by_name('username') #find element by name
    print("My input element is:")
    print(username)
    driver.close()
    # My input element is:
    # <selenium.webdriver.remote.webelement.WebElement (session="6f92b4105aa5067d479892158a7d8a3c", element="bede9793-c506-4a44-a2e7-1370a30fbb75")>


# Find Element Based on class tag
def parse_by_class(driver):
    content = driver.find_element_by_class_name("content")
    print("My class element is:")
    print(content)
    driver.close()
    # My class element is:
    # <selenium.webdriver.remote.webelement.WebElement (session="fbd0b2d33726c508ba169f8f8dda371a", element="5a8d22ba-decc-490c-9b1b-dfbb38842fa6")>ss


# Finding Elements By XPath (XML path Language)
#  ***SHOULD ONLY BE USED IF NAME, ID OR CLASS IS NOT AVAILABLE***
# XPath - Follows a Tree or folder structure making it easy to parse, 
# XPATH of elements can be found below the element tree in chrome devtools by selecting the element
def parse_by_XPath(driver):
    login_form_absolute = driver.find_element_by_xpath("/html/body/form[1]")# Try to avoid absolute paths, as changes in structure can break them
    login_form_relative = driver.find_element_by_xpath("//form[1]")# find the first form element on the third level
    login_form_id = driver.find_element_by_xpath("//form[@id='loginForm']") #More specific find form with id "login form" on third level

    print("My login form is:")
    print(login_form_absolute)
    print(login_form_relative)
    print(login_form_id)
    driver.close()


def main():
    driver = webdriver.Chrome() #Open a new browser instance selecting the browser driver to use
    #Web Drivers(Must be a path var to work.): Chrome, Firefox, Internet Explorer, Safari, Edge

    dir = os.getcwd().replace('\\',"/") + "/html_code_02.html" #used to avoid absolute path for git

    # driver.get("http://www.python.org") #for live websites
    driver.get('file:///'+dir) #Open the file
    parse_by_id(driver)
    # parse_by_name(driver)
    # parse_by_class(driver)
    # parse_by_XPath(driver)
    
#C:\Users\curti\Desktop\PythonGroundUp\Automation and Testing Selenium\Chapter 2 - Parsing the HTML DOM Structure\html_code_02.html
if __name__ == "__main__":
    main()