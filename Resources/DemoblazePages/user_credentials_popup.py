from selenium.webdriver.common.by import By
from .base_page import BasePage


class UserCredentialsBasePopup(BasePage):
    def __init__(self, driver, user_name_locator, password_locator):
        self.user_name_textbox_locator = user_name_locator
        self.password_textbox_locator = password_locator
        super().__init__('', driver)

    def fill_username_textbox(self, username):
        self.driver.find_element(*self.user_name_textbox_locator).send_keys(username)

    def fill_password_textbox(self, password):
        self.driver.find_element(*self.password_textbox_locator).send_keys(password)


class SignUpPopup(UserCredentialsBasePopup):
    def __init__(self, driver):
        user_name_textbox_locator = (By.ID, 'sign-username')
        password_textbox_locator = (By.ID, 'sign-password')
        self.signup_button_locator = (By.XPATH, "//button[@onclick='register()']")
        super().__init__(driver, user_name_textbox_locator, password_textbox_locator)

    def signup(self, user_name, password):
        self.fill_username_textbox(user_name)
        self.fill_password_textbox(password)
        super().scroll_and_click(self.signup_button_locator)


class LoginPopup(UserCredentialsBasePopup):
    def __init__(self, driver):
        user_name_textbox_locator = (By.ID, 'loginusername')
        password_textbox_locator = (By.ID, 'loginpassword')
        self.login_button_locator = (By.XPATH, "//div[@class='modal fade show']//button[@class='btn btn-primary']")
        super().__init__(driver, user_name_textbox_locator, password_textbox_locator)

    def login(self, user_name, password):
        self.fill_username_textbox(user_name)
        self.fill_password_textbox(password)
        super().scroll_and_click(self.login_button_locator)
