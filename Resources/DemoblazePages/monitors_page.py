from selenium.webdriver.common.by import By
import re
from .base_page import BasePage


class MonitorsPage(BasePage):
    def __init__(self, driver):
        super().__init__('#', driver)
        self.prices_locator = (By.XPATH, "//h4[@class='card-title']/following-sibling::h5")

    def open_highest_priced_product(self):
        super().wait_page_url()
        super().wait_page_ready()

        price_texts = []
        products_cards = self.driver.find_elements(By.XPATH, ".//*[@class='card h-100']")
        for product_card in products_cards:
            price_element = product_card.find_element(*self.prices_locator)
            price_texts.append(float(re.sub(r'[^\d.]', '', price_element.text)))
        max_price = max(price_texts)
        max_price_index = price_texts.index(max(price_texts))
        max_price_product = products_cards[max_price_index]
        product_title_element = max_price_product.find_element(By.XPATH, ".//h4[@class='card-title']/a")
        max_title = product_title_element.text
        super().click_element(product_title_element)
        return max_price, max_title
