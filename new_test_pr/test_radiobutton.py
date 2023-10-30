import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://demoqa.com/radio-button')
driver.maximize_window()
time.sleep(2)
radiobutton = driver.find_element(By.XPATH, "//label[@for='impressiveRadio']")
radiobutton.click()
time.sleep(5)
