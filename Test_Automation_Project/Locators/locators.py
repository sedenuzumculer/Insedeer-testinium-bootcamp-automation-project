from selenium.webdriver.common.by import By


class HomePageLocators:
    """A class for main page locators. All main page locators should come here"""

    SEARCH_BOX = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    SECOND_PAGE_LINK = (By.CSS_SELECTOR, 'a[aria-label="2 sayfasına git"]')
    COOKIE_BANNER_ACCEPT_BUTTON = (By.ID, 'sp-cc-accept')
    FIFTH_ROW_FIRST_PRODUCT = (By.XPATH, '(//div[contains(@class, "s-main-slot")]//div['
                                         '@data-component-type="s-search-result"])[13]//a[@class="a-link-normal '
                                         's-no-outline"]')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'input.a-button-input[data-ref]')
    SHOPPING_CART_BUTTON = (By.ID, 'nav-cart-count-container')
    AMAZON_LOGO = (By.ID, 'nav-logo-sprites')


