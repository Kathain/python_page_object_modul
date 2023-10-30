import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://demoqa.com/dynamic-properties')
driver.maximize_window()
try:
    visible_button = driver.find_element(By.CSS_SELECTOR, '#visibleAfter')
    visible_button.click()
    print('Click Visible Button')
except NoSuchElementException as exception:
    print('NoSuchElementException')
    time.sleep(10)
    visible_button = driver.find_element(By.CSS_SELECTOR, '#visibleAfter')
    visible_button.click()

