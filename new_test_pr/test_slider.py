import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('https://html5css.ru/howto/howto_js_rangeslider.php')
driver.maximize_window()
time.sleep(20)
action = ActionChains(driver)
slider = driver.find_element(By.CSS_SELECTOR, '#id1')
action.click_and_hold(slider).move_by_offset(20, 0).release().perform()
time.sleep(3)
