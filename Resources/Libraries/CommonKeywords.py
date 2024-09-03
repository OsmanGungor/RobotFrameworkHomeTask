from selenium import webdriver
from robot.api.deco import keyword

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(root_path)

from Resources.DemoblazePages.index_page import IndexPage
from Resources.DemoblazePages.cart_page import CartPage
from Resources.DemoblazePages.monitors_page import MonitorsPage
from Resources.DemoblazePages.prod_page import ProdPage
from Resources.DemoblazePages.user_credentials_popup import SignUpPopup, LoginPopup
from listeners.ScreenshotListener import ScreenshotListener


class CommonKeywords:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CommonKeywords, cls).__new__(cls, *args, **kwargs)
            cls._instance.driver = None
        return cls._instance

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = ScreenshotListener()

    def open_browser(self, browser='chrome'):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def close_browser(self):
        if self.driver:
            self.driver.quit()

    def open_browser_and_signup(self, user_name, user_pass, browser='chrome'):
        self.open_browser(browser)
        index_page = IndexPage(self.driver)
        index_page.open_page()
        index_page.click_signup()
        signup_popup = SignUpPopup(self.driver)
        signup_popup.signup(user_name, user_pass)

    def open_browser_and_login(self, user_name, user_pass, browser='chrome'):
        self.open_browser(browser)
        self.setup_login(user_name, user_pass)

    def setup_login(self, user_name, user_pass):
        self.click_login()
        self.populate_login_popup_click(user_name, user_pass)

    @keyword(tags=["screenshot"])
    def click_login(self):
        index_page = IndexPage(self.driver)
        index_page.open_page()
        index_page.click_login()

    def populate_login_popup_click(self, user_name, user_pass):
        login_popup = LoginPopup(self.driver)
        index_page = IndexPage(self.driver)
        login_popup.login(user_name, user_pass)
        index_page.wait_element_displayed(index_page.welcome_message_locator)

    def assert_login_textboxes(self):
        login_popup = LoginPopup(self.driver)
        login_popup.wait_element_displayed(login_popup.user_name_textbox_locator)
        login_popup.wait_element_displayed(login_popup.password_textbox_locator)

    @keyword(tags=["screenshot"])
    def get_welcome_text(self):
        index_page = IndexPage(self.driver)
        return index_page.get_welcome_text()

    @keyword(tags=["screenshot"])
    def get_most_expensive_monitor(self):
        index_page = IndexPage(self.driver)
        index_page.click_monitors()
        monitors_page = MonitorsPage(self.driver)
        max_price, max_title = monitors_page.open_highest_priced_product()
        product_page = ProdPage(self.driver)
        product_page.wait_page_ready()
        return max_price, max_title

    def add_product_to_cart(self):
        product_page = ProdPage(self.driver)
        product_page.add_to_chart()

    def get_name_price_at_product_page(self):
        product_page = ProdPage(self.driver)
        return product_page.get_product_name()

    @keyword(tags=["screenshot"])
    def get_products_at_cart(self):
        cart_page = CartPage(self.driver)
        cart_page.open_page()
        cart_products = cart_page.get_products()
        return cart_products
