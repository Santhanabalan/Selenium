from selenium import webdriver  
from nose.tools import *
import time
print("sample test case started")  
driver = webdriver.Chrome(r"D:\Developer_Zone\Selenium\Demo\chromedriver.exe") 
driver.maximize_window()   
driver.get("https://santhanabalan.github.io/Selenium/") 
time.sleep(3)   
driver.find_element_by_xpath('/html/body/div/button/a').click()
actualUrl="https://santhanabalan.github.io/Selenium/success1.html"
expectedUrl= driver.current_url 
assert_equal(actualUrl,expectedUrl)
driver.close()  
print("Test Completed Succesfully")  