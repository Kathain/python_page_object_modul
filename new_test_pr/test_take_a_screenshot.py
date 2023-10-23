import datetime
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
time.sleep(2)
button_login.click()
now_date = datetime.datetime.utcnow().strftime(' %Y.%m.%d. %H:%M')
name_screenshot = 'screenshot' + now_date + '.png'
driver.save_screenshot('screenshots/' + name_screenshot)

# driver.save_screenshot(f"1screenshot {now_date}.png")  можно сделать просто через f строку
