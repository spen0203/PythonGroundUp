from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select #Select class import
import time

driver = webdriver.Chrome() 

driver.get('https://wiki.python.org/moin/FrontPage') #Open the file html_code_03

#Search for "Beginner"
searchBar = driver.find_element_by_id('searchinput')
searchBar.send_keys("Beginner")
searchBar.send_keys(Keys.RETURN)
time.sleep(4)


#Select More actions: Raw Text
select = Select(driver.find_element_by_xpath('//*[@id="sidebar"]/div[3]/ul/li[5]/form/div/select')) #No ID or Name so used XPath
time.sleep(4)
select.select_by_value("raw")
time.sleep(4)

driver.close()

