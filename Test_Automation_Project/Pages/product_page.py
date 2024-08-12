from Pages.base_page import BasePage
from Locators.locators import HomePageLocators


class ProductPage(BasePage):
    def accept_cookies(self):
        try:
            self.click_element(HomePageLocators.COOKIE_BANNER_ACCEPT_BUTTON)
        except Exception as e:
            print(f"Cookie kabul button tıklanamadı: {e}")
            pass

    def go_to_second_page(self):
        return self.click_element(HomePageLocators.SECOND_PAGE_LINK)

    def verify_on_second_page(self):
        assert "page=2" in self.get_current_url(), "2. sayfada değil."

    def click_fifth_row_first_product(self):
        self.click_element(HomePageLocators.FIFTH_ROW_FIRST_PRODUCT)


class ProductPageNew(BasePage):
    def verify_on_correct_product_page(self, expected_product_id):
        current_url = self.get_current_url()
        assert expected_product_id in current_url, f"Expected product ID '{expected_product_id}' not in URL '{current_url}'"

    def add_product_to_cart(self):
        # Assuming there is a locator defined for the button you want to click
        self.click_element(HomePageLocators.ADD_TO_CART_BUTTON)