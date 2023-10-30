import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://demoqa.com/buttons')
driver.maximize_window()
time.sleep(2)
action = ActionChains(driver)
button_for_click = driver.find_element(By.CSS_SELECTOR, "#doubleClickBtn")
button_for_click.click()
action.double_click(button_for_click).perform()
# perform нужно для того что бы сохранить результат
right_click = driver.find_element(By.CSS_SELECTOR, '#rightClickBtn')
right_click.click()
action.context_click(right_click).perform()
time.sleep(5)
