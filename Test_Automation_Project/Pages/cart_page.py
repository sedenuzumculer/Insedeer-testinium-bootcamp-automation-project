from Pages.base_page import BasePage
from Locators.locators import HomePageLocators


class CartPage(BasePage):
    def sopping_cart_click(self):
        return self.click_element(HomePageLocators.SHOPPING_CART_BUTTON)

    def main_logo_click(self):
        return self.click_element(HomePageLocators.AMAZON_LOGO)
