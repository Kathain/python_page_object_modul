from selenium import webdriver
from oop_plus_selenium.login_page_test_3 import Login_Page_Test_3


class Test03:

    def test_login(self):
        driver = webdriver.Chrome()
        driver.get('https://www.saucedemo.com/')
        driver.maximize_window()
        print('Start Test')
        list_of_users = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
        login_password = 'secret_sauce'
        login = Login_Page_Test_3(driver)    # логин является ЭК логин пэйдж и указываем наш драйвер
        for i in list_of_users:
            login.authorization(i, login_password)

test = Test03()
test.test_login()

