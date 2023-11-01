from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_Page_Test_3:
    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login_name, login_password):
        user_name_input = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#user-name')))
        user_name_input.send_keys(login_name)
        print("Input Login")

        password_input = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#password')))
        password_input.send_keys(login_password)
        print("Input Password")

        button_login = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#login-button')))
        button_login.click()
        print("Click Login Button")

        if login_name == 'locked_out_user':
            print('Error here')
            error_msg = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//h3[@data-test='error']")))
            value_error_msg = error_msg.text
            assert value_error_msg == 'Epic sadface: Sorry, this user has been locked out.', 'Error message is NOT correct'
            print('Error message is Correct!')
            user_name_input.send_keys(Keys.BACKSPACE * len(login_name))
            password_input.send_keys(Keys.BACKSPACE * len(login_password))
            return

        title_products = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        value_title_products = title_products.text
        assert value_title_products == "Products", 'Title is NOT correct'
        print('Title on the main page is Correct!')

        menu_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#react-burger-menu-btn')))
        menu_button.click()
        print("Click Menu")

        logout_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#logout_sidebar_link')))
        logout_button.click()
        print("Logout")
