import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# get the path of ChromeDriverServer
dir = os.path.dirname(__file__)
chrome_driver_path = "C:/Users/Aman\Downloads\Compressed\chromedriver_win32\chromedriver.exe"

# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get("http://www.csgoatse.com")
# get the search textbox
sf = driver.find_element_by_class_name("btn-login")

sf.click()
# enter search keyword and submit
username = driver.find_element_by_id("steamAccountName")
password = driver.find_element_by_id("steamPassword")
submit = driver.find_element_by_id("imageLogin")
username.send_keys( "" )
password.send_keys("")
submit.click()
