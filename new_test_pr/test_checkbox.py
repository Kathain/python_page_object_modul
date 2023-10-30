import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://demoqa.com/checkbox')
driver.maximize_window()
time.sleep(2)
checkbox = driver.find_element(By.XPATH, "//span[@class='rct-checkbox']")
checkbox.click()
time.sleep(5)
checkbox2 = driver.find_element(By.XPATH, "//button[@aria-label='Toggle']")
checkbox2.click()
time.sleep(5)