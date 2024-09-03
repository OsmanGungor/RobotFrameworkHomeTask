from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class ProdPage(BasePage):
    def __init__(self, driver):
        super().__init__('prod.html', driver)
        self.add_to_cart_button_locator = (By.XPATH, "//*[contains(@onclick,'addToCart')]")
        self.product_name_locator = (By.XPATH, "//h2[@class='name']")
        self.product_price_locator = (By.XPATH, "//h3[@class='price-container']")

    def add_to_chart(self):
        super().wait_page_url()
        super().wait_page_ready()
        super().scroll_and_click(self.add_to_cart_button_locator)
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            print("Alert present: " + alert.text)
            alert.accept()  # Accept the alert
        except TimeoutException:
            print("No alert present within the timeout period.")

    def get_product_name(self):
        return self.driver.find_element(*self.product_name_locator).text
