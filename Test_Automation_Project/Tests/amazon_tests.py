import time

from Pages.home_page import HomePage
from Pages.product_page import ProductPage
from Tests.base_tests import BaseTest
from Pages.product_page import ProductPageNew
from Pages.cart_page import CartPage


class AmazonTests(BaseTest):
    def test_amazon_tests(self):
        home_page = HomePage(self.driver)
        self.assertEqual(self.base_url, home_page.get_current_url(), "Amazon Anasayfa Açılamadı")
        home_page.search_for_item("samsung")
        time.sleep(1)
        home_page.search_item_click()
        time.sleep(2)

        product_page = ProductPage(self.driver)
        product_page.accept_cookies()
        time.sleep(1)
        product_page.go_to_second_page()
        time.sleep(1)
        product_page.verify_on_second_page()
        time.sleep(2)

        product_page.click_fifth_row_first_product()
        time.sleep(1)
        product_page_new = ProductPageNew(self.driver)
        product_page_new.add_product_to_cart()
        cart_page = CartPage(self.driver)
        cart_page.sopping_cart_click()
        time.sleep(2)
        self.assertIn("cart", cart_page.get_current_url(), "Shopping cart page not opened.")
        cart_page.main_logo_click()



