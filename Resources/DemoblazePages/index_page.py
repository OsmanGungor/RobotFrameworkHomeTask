from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class IndexPage(BasePage):
    def __init__(self, driver):
        super().__init__('', driver)
        self.index_logo_locator = (By.ID, 'nava')
        self.welcome_message_locator = (By.ID, 'nameofuser')
        self.login_locator = (By.ID, 'login2')
        self.logout_locator = (By.ID, 'logout2')
        self.signup_locator = (By.ID, 'signin2')
        self.monitors_tab_locator = (By.XPATH, '//a[@onclick="byCat(\'monitor\')"]')

    def open_page(self):
        super().open_page()
        assert WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.index_logo_locator))

    def click_login(self):
        super().scroll_and_click(self.login_locator)

    def click_signup(self):
        super().scroll_and_click(self.signup_locator)

    def click_monitors(self):
        super().scroll_and_click(self.monitors_tab_locator)

    def get_welcome_text(self):
        welcome_element = self.driver.find_element(*self.welcome_message_locator)
        return welcome_element.text
