from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import allure_log

class ProductPage(BasePage):
    ADD_TO_CART = (By.XPATH, "//a[contains(text(),'Add to cart')]")

    def buy_product(self):
        
        allure_log("buy_product")

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.ADD_TO_CART)
        )
        allure_log("buy_product1")
        self.click(self.ADD_TO_CART)
