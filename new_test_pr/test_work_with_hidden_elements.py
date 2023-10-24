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
button_login = driver.find_element(By.CSS_SELECTOR, '#login-button')
time.sleep(3)
button_login.click()

menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
menu.click()
time.sleep(3)
link_about = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
time.sleep(3)
link_about.click()
time.sleep(3)
