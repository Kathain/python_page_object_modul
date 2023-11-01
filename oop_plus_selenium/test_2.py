import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from oop_plus_selenium.login_page import Login_Page


class Test02:

    def test_select_product(self):
        driver = webdriver.Chrome()
        driver.get('https://www.saucedemo.com/')
        driver.maximize_window()
        print('Start Test')
        login_problem_user = 'problem_user'
        password_all = 'secret_sauce'
        login = Login_Page(driver)    # логин является ЭК логин пэйдж и указываем наш драйвер
        login.authorization(login_problem_user, password_all)    # вызываем метод который в классе Логин Пэйдж и передаем туда атрибуты

        select_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#add-to-cart-sauce-labs-backpack')))
        select_product.click()
        print('Click Select Product')
        cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.shopping_cart_link')))
        cart.click()
        print('Enter shopping cart')
        success_test = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='title']")))
        value_success_test = success_test.text
        assert value_success_test == 'Your Cart'
        print('Test Success!!!')

test = Test02()
test.test_select_product()
