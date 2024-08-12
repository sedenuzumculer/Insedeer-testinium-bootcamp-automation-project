from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=20)

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        element = self.wait.until(ec.element_to_be_clickable(*locator))
        element.click()

    def select_element(self, *locator, option_text):
        select = Select(self.find(*locator))
        select.select_by_visible_text(option_text)

    def get_current_url(self):
        return self.driver.current_url

    def enter_text(self, locator, text):
        element = self.find(*locator)
        element.clear()
        element.send_keys(text)
