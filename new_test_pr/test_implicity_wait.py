import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://demoqa.com/dynamic-properties')
driver.implicitly_wait(10)     # делаем не явное ожидание которое
# распостраняется на весь тест (не нужно больше писать тайм.sleep)
try:
    visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
    visible_button.click()
    print('Click Visible Button')
except NoSuchElementException as exception:
    print('NoSuchElementException')


