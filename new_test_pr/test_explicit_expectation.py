import time
from telnetlib import EC

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://demoqa.com/dynamic-properties')

try:
    visible_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(()))
    visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
    visible_button.click()
    print('Click Visible Button')
except NoSuchElementException as exception:
    print('NoSuchElementException')


