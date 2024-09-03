from selenium.webdriver.common.by import By
from .base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__('cart.html', driver)
        self.table_rows_locator = (By.XPATH, '//tbody/tr')

    def get_products(self):
        products = []
        rows = self.get_all_product_rows()
        if not rows:
            return products

        for row in rows:
            title_cell = row.find_element(By.XPATH, 'td[2]').text
            price_cell = float(row.find_element(By.XPATH, 'td[3]').text)
            products.append((title_cell, price_cell))

        return products

    def get_all_product_rows(self):
        super().wait_page_url()
        super().wait_page_ready()

        rows = self.driver.find_elements(*self.table_rows_locator)
        return rows

    def empty_cart(self):
        rows = self.get_all_product_rows()
        while rows:
            row = rows[0]
            delete_link = row.find_element(By.XPATH, "//a[contains(@onclick,'deleteItem')]")
            super().click_element(delete_link)
            rows = self.get_all_product_rows()

