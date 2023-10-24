import datetime
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
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

# driver.execute_script("window.scroll(0,500)")    # скрипт для скроллинга (он не работает в паре со скриптом ниже)

action = ActionChains(driver)   # делаем переменную в котором мы указываем каким браузером мы хотим управлять
time.sleep(5)
red_tshirt = driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
action.move_to_element(red_tshirt).perform()   # указываем что нам нужно именно до этого элемента скролить
time.sleep(5)
red_tshirt.click()

now_date = datetime.datetime.utcnow().strftime(' %Y.%m.%d. %H:%M')
name_screenshot = 'screenshot' + now_date + '.png'
driver.save_screenshot('screenshots/' + name_screenshot)

