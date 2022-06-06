from selenium import webdriver  
from nose.tools import *
import time
print("Sample test case started")  
driver = webdriver.Chrome(r"D:\Developer_Zone\Selenium\Demo\chromedriver.exe") 
driver.maximize_window()   
driver.get("https://santhanabalan.github.io/Selenium/")   
driver.find_element_by_name("username").send_keys("Admin")  
time.sleep(3)  
driver.find_element_by_name("password").send_keys("12345")   
time.sleep(3) 
driver.find_element_by_xpath('//*[@id="submit"]').click() 
time.sleep(3) 
actualUrl="https://santhanabalan.github.io/Selenium/success.html"
expectedUrl= driver.current_url 
assert_equal(actualUrl,expectedUrl)
driver.close()  
print("Test Completed Succesfully")  