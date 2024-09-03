import time
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, url, driver):
        self.driver = driver
        self.baseurl = 'https://www.demoblaze.com/'
        self.url = self.baseurl + url

    def open_page(self):
        if self.url in self.driver.current_url:
            self.driver.refresh()
        else:
            self.driver.get(self.url)
            self.wait_page_url()
        self.wait_page_ready()

    def wait_page_url(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver:  self.url in driver.current_url,
                   f"Page url is expected to be {self.url}")

    def wait_page_ready(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete",
                   f"Page is not in readyState 'complete'")
        time.sleep(1)

    def wait_element_displayed(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: driver.find_element(*locator).get_attribute("style") != "display: none;",
                   f"Element is not displayed: {locator}"
                   )

    def scroll_to_element(self, locator, retries=3, delay=2):
        for attempt in range(retries):
            try:
                element = self.driver.find_element(*locator)
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                time.sleep(1)
                return element
            except (StaleElementReferenceException, NoSuchElementException):
                time.sleep(delay)
        raise Exception(f"Unable to locate and scroll to the element after {retries} attempts.")

    def scroll_and_click(self, locator, retries=3, delay=2):
        self.wait_element_displayed(locator)
        for attempt in range(retries):
            try:
                element = self.scroll_to_element(locator)
                element.click()
                return
            except (StaleElementReferenceException, NoSuchElementException):
                time.sleep(delay)
        raise Exception(f"Unable to click on the element after {retries} attempts")

    def click_element(self, element, retries=3, delay=2):
        for attempt in range(retries):
            try:
                element.click()
                return
            except (StaleElementReferenceException, NoSuchElementException):
                time.sleep(delay)
        raise Exception(f"Unable to click on the element after {retries} attempts")
