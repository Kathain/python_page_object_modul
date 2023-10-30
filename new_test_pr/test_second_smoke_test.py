import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""LOG IN"""
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
value_product_1 = product_1.text          # значение первого продукта
print(value_product_1)
product_2 = driver.find_element(By.CSS_SELECTOR, '#item_2_title_link')
value_product_2 = product_2.text          # значение второго продукта
print(value_product_2)

price_product_1 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[1]")
value_price_pr_1 = price_product_1.text    # цена первого продукта
print(value_price_pr_1)
price_product_2 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[5]")
value_price_pr_2 = price_product_2.text    # цена второго продукта
print(value_price_pr_2)

select_pr_1 = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
select_pr_1.click()       # добавили в корзину первый продукт
select_pr_2 = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie')
select_pr_2.click()        # добавили в корзину второй продукт
cart = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
cart.click()               # перешли в корзину
time.sleep(3)

"""INFO CART PRODUCT 1"""

cart_product_1 = driver.find_element(By.CSS_SELECTOR, '#item_4_title_link')
value_cart_product_1 = cart_product_1.text      # ищем значение первого продукта
print(value_cart_product_1)
cart_product_2 = driver.find_element(By.CSS_SELECTOR, '#item_2_title_link')
value_cart_product_2 = cart_product_2.text      # ищем значение второго продукта
print(value_cart_product_2)
assert value_product_1 == value_cart_product_1, 'Info Cart PR1 is NOT Correct'
# проверка что значения
# первого продукта совпадают
assert value_product_2 == value_cart_product_2, 'Info Cart PR2 is NOT Correct'
# проверка что значения
# второго продукта совпадают
cart_price_product_1 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[1]")
value_cart_price_pr_1 = cart_price_product_1.text
# поиск цены первого продукта в корзине
print(value_cart_price_pr_1)
cart_price_product_2 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[2]")
value_cart_price_pr_2 = cart_price_product_2.text
# поиск цены второго продукта в корзине
print(value_cart_product_2)

assert value_price_pr_1 == value_cart_price_pr_1, 'Price PR1 in Cart is NOT Correct'
assert value_price_pr_2 == value_cart_price_pr_2, 'Price PR 2 in Cart is NOT Correct'
checkout_button = driver.find_element(By.CSS_SELECTOR, '#checkout')
checkout_button.click()

"""CHECKOUT PAGE INFO"""

first_name_checkout = driver.find_element(By.CSS_SELECTOR, '#first-name')
first_name_checkout.send_keys('Test')
print(first_name_checkout)
last_name_checkout = driver.find_element(By.CSS_SELECTOR, '#last-name')
last_name_checkout.send_keys('Testov')
print(last_name_checkout)
zip_code = driver.find_element(By.CSS_SELECTOR, '#postal-code')
zip_code.send_keys('123456')
print(zip_code)
button_continue = driver.find_element(By.CSS_SELECTOR, '#continue')
button_continue.click()

"""CHECKOUT OVERVIEW PAGE"""

overview_product_1 = driver.find_element(By.CSS_SELECTOR, '#item_4_title_link')
value_overview_product_1 = overview_product_1.text
print(value_overview_product_1)
overview_product_2 = driver.find_element(By.CSS_SELECTOR, '#item_2_title_link')
value_overview_product_2 = overview_product_2.text
print(value_overview_product_2)

assert value_overview_product_1 == value_cart_product_1, 'Info Cart PR1 is NOT Correct'
assert value_overview_product_2 == value_cart_product_2, 'Info Cart PR2 is NOT Correct'

overview_price_product_1 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[1]")
value_overview_price_pr_1 = overview_price_product_1.text
print(value_overview_price_pr_1)
overview_price_product_2 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[2]")
value_overview_price_pr_2 = overview_price_product_2.text
print(value_overview_price_pr_2)
assert value_overview_price_pr_1 == value_cart_price_pr_1, 'Price PR1 is NOT correct'
assert value_overview_price_pr_2 == value_cart_price_pr_2, 'Price PR2 is NOT correct'

list_values = [value_overview_price_pr_1, value_overview_price_pr_2]
list_of_price = []
for i in list_values:
    list_of_price.append(float(i[1:]))
    result = sum(list_of_price)
print(result)

item_total = driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
value_item_total = item_total.text
print(value_item_total)
value_of_split = value_item_total.split(' ')
print(value_of_split)
price_value_with_sub = value_of_split[-1]
print(price_value_with_sub)
result_items_total = float(price_value_with_sub[1:])
print(result_items_total)
assert result_items_total == result, 'Sum is NOT Correct'
print('Sum is CORRECT')
finish_button = driver.find_element(By.CSS_SELECTOR, '#finish')
finish_button.click()
time.sleep(3)
print('Final')