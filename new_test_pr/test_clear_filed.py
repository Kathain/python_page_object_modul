import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
time.sleep(2)
user_name = driver.find_element(By.CSS_SELECTOR, '#user-name')
user_name.send_keys('standard_user')
password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys('secret_sauce')
time.sleep(5)
user_name.clear()
time.sleep(5)
password.clear()
time.sleep(5)



