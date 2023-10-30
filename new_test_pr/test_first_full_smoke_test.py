import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
time.sleep(2)
user_name = driver.find_element(By.CSS_SELECTOR, '#user-name')
user_name.send_keys('standard_user')
password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys('secret_sauce')
button_login = driver.find_element(By.CSS_SELECTOR, '#login-button')
time.sleep(3)
button_login.click()
"""INFO Product 1"""
product_1 = driver.find_element(By.CSS_SELECTOR, '#item_4_title_link')
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[1]")
value_price_pr_1 = price_product_1.text
print(value_price_pr_1)

select_pr_1 = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
select_pr_1.click()
cart = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
cart.click()
time.sleep(3)

"""INFO CART PRODUCT 1"""

cart_product_1 = driver.find_element(By.CSS_SELECTOR, '#item_4_title_link')
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1, 'Info Cart PR1 is NOT Correct'
cart_price_product_1 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[1]")
value_cart_price_pr_1 = cart_price_product_1.text
print(value_cart_price_pr_1)
assert value_price_pr_1 == value_cart_price_pr_1, 'Price in Cart is NOT Correct'
