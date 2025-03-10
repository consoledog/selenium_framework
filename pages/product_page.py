from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART = (By.XPATH, "//a[contains(text(),'Add to cart')]")

    def buy_product(self):
        self.click(self.ADD_TO_CART)
