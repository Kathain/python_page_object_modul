import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select




driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
time.sleep(2)
user_name = driver.find_element(By.CSS_SELECTOR, '#user-name')
user_name.send_keys('standard_user')
time.sleep(0.5)
user_name.send_keys(Keys.BACKSPACE)  # нажимаем клавишу бэкспейс и удаляем последнюю букву
time.sleep(0.5)
user_name.send_keys(Keys.BACKSPACE)  # нажимаем клавишу бэкспейс и удаляем еще одну букву
time.sleep(0.5)
user_name.send_keys('er')  # вставляем обратно удаленные буквы
password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys('secret_sauce')
password.send_keys(Keys.ENTER)
time.sleep(4)
filter = driver.find_element(By.XPATH, "//select[@data-test='product_sort_container']")
filter.click()
time.sleep(4)
select_filter = Select(filter)
select_filter.select_by_index(2)
time.sleep(4)
filter.send_keys(Keys.RETURN)
time.sleep(4)



