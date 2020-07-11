from selenium import webdriver
from selenium.webdriver.support.ui import Select #Select class import
from selenium.webdriver import ActionChains

import time
import os

#############################################
## Navigating through Pages Using Selenium:
# 
# Interactions Possible: 
#       Select, Submit , Drag&drop, hover
#############################################

def DragandDropElements(driver):
    driver.get('http://jqueryui.com/droppable') #open webpage
    driver.switch_to.frame(0) #switch to frame with UI
    action_chains= ActionChains(driver) #create and actionChains instance, automate:drag&drop, hover etc
    
    source= driver.find_element_by_id('draggable')
    target = driver.find_element_by_id('droppable')

    action_chains.drag_and_drop_by_offset(source, 100, 100).perform() #move by predefined amount
    time.sleep(2)

    action_chains.drag_and_drop(source, target).perform() #move to specific element
    time.sleep(2)

    driver.close()

#Selecting Items by: Index, Visible text, Value
def SelectandSubmitElements(driver):
    select = Select(driver.find_element_by_name('numReturnSelect')) #Create an instance of select element from html
    select.select_by_index(4) #index in array
    time.sleep(2)
    select.select_by_visible_text("200") #visible text
    time.sleep(2)
    select.select_by_value("250") #value tag
    time.sleep(2)
    
    options = select.options #list all potention element options
    print(options)

    submit_button = driver.find_element_by_name('continue') #find the submit button
    submit_button.submit(); #Submit it
    time.sleep(2)

    driver.close()



def main():
    driver = webdriver.Chrome() 
    dir = os.getcwd().replace('\\',"/") + "/html_code_03.html" #used to avoid absolute path for git
    driver.get('file:///'+dir) #Open the file html_code_03

    SelectandSubmitElements(driver)
    
if __name__ == "__main__":
    main()