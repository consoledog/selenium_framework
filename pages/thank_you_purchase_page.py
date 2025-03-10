from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ThankyouPage(BasePage):
    GREETING_MESSAGE = (By.XPATH, "//h2[contains(text(),'Thank you for your purchase!')]")
    OK_BUTTON = (By.XPATH, "//button[contains(text(),'OK')]")

    def getGreetingMessage(self) -> str:
        return self.get_text(self.GREETING_MESSAGE)
    def clickOk(self):
        return self.click(self.OK_BUTTON)