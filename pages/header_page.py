from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HeaderPage(BasePage):
    HOME = (By.PARTIAL_LINK_TEXT, "Home")
    CONTACT = (By.LINK_TEXT, "Contact")
    ABOUT_US = (By.LINK_TEXT, "About us")
    CART = (By.ID, "cartur")
    LOGIN = (By.ID, "login2")
    SING_UP = (By.ID, "signin2")

    def click_on_cart(self):
        self.click(self.CART)