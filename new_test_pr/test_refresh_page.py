import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
url = 'https://www.saucedemo.com/'
driver.get(url)
driver.maximize_window()

login = 'wrong user'
password_all = 'secret_sauce'

user_name = driver.find_element(By.CSS_SELECTOR, '#user-name')
user_name.send_keys(login)
password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys(password_all)
button_login = driver.find_element(By.CSS_SELECTOR, '#login-button')
time.sleep(2)
button_login.click()
time.sleep(5)
warning_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warning_test = warning_text.text
assert value_warning_test == 'Epic sadface: Username and password do not match any user in this service'
time.sleep(5)
driver.refresh()                    # обновили станицу
time.sleep(5)
