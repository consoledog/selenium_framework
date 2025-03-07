from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_BUTTON = (By.ID, "login2")
    USERNAME = (By.ID, "loginusername")
    PASSWORD = (By.ID, "loginpassword")
    SUBMIT = (By.XPATH, "//button[contains(text(),'Log in')]")
    WELCOME = (By.ID, "nameofuser")

    def login(self, username, password):
        self.click(self.LOGIN_BUTTON)
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)
