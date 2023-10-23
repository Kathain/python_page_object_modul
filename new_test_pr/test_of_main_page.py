import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
url = 'https://www.saucedemo.com/'
driver.get(url)
driver.maximize_window()

login = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element(By.CSS_SELECTOR, '#user-name')
user_name.send_keys(login)
password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys(password_all)
button_login = driver.find_element(By.CSS_SELECTOR, '#login-button')
time.sleep(2)
button_login.click()

#text_products = driver.find_element(By.XPATH, "//span[@class='title']")
#value_text_products = text_products.text
#assert value_text_products == 'Products', 'Error, you are not on Products page'
main_page_url = 'https://www.saucedemo.com/inventory.html'
get_url = driver.current_url
assert main_page_url == get_url, 'Not correct product page url'

