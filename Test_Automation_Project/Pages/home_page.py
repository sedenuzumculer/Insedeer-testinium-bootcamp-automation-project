from Locators.locators import HomePageLocators
from Pages.base_page import BasePage


class HomePage(BasePage):
    def search_for_item(self, item):
        self.enter_text(HomePageLocators.SEARCH_BOX, item)

    def search_item_click(self):
        return self.click_element(HomePageLocators.SEARCH_ICON)

