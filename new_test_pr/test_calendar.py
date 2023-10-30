import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get('https://demoqa.com/date-picker')
driver.maximize_window()
time.sleep(2)
new_date = driver.find_element(By.CSS_SELECTOR,'#datePickerMonthYearInput')
new_date.send_keys(Keys.BACKSPACE * 10)
new_date.click()
time.sleep(3)
new_date_2 = driver.find_element(By.XPATH, 'div[aria-label="Choose Tuesday, August 8th, 2023"]')
new_date_2.click()
time.sleep(3)
