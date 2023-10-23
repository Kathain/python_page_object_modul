import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
time.sleep(2)
user_name = driver.find_element(By.CSS_SELECTOR, '#user-name')
user_name.send_keys('standard_user')
time.sleep(5)
user_name.send_keys(Keys.BACKSPACE)  # нажимаем клавишу бэкспейс и удаляем последнюю букву
time.sleep(5)
user_name.send_keys(Keys.BACKSPACE)  # нажимаем клавишу бэкспейс и удаляем еще одну букву
time.sleep(5)
user_name.send_keys('er')  # вставляем обратно удаленные буквы

#password = driver.find_element(By.CSS_SELECTOR, '#password')
#password.send_keys('secret_sauce')
#button_login = driver.find_element(By.CSS_SELECTOR, '#login-button')
#time.sleep(15)
#button_login.click()



