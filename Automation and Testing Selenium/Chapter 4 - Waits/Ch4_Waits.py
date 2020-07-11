#############################################
## Waits on Pages Using Selenium:
# 
# Not all web componenets load at the same pace, 
# ** IF a script launches and cant find the required component it will fail **
#
# Explicit Wait:
#   - Stop execution until a condition is met
#       Wait for an image to load, alert to be present, text to be present
# Implicit Wait:
#   - Poll the DOM for a given time for each step of the script, if a step takes longer throw an error
#
#############################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #Used for ExplicitWait
from selenium.webdriver.support import expected_conditions as EC #Used for ExplicitWait


# Wait 10 seconds for element to load, if it doesn't load in time throw timeout exception
def ExplicitWait(driver):
    try:
        element = WebDriverWait(driver, 10).until( #Adds a 10 sec wait to driver
            EC.presence_of_element_located((By.ID, "start-shell")) #if this doesn't load in 10 secs itll timeout exception
        )
    finally:
        driver.quit()


# Wait a maximum 10 seconds between each step or throw an error
def ImplicitWait(driver):
    driver.implicitly_wait(10) #specified in seconds implicit wait
    driver.get('http://www.python.org')
    myDynamicElement = driver.find_element_by_id('start-shell')
    driver.close()

def main():
    driver= webdriver.Chrome()
    driver.get('http://www.python.org')
    #ExplicitWait(driver)
    ImplicitWait(driver)


if __name__ == "__main__":
    main()