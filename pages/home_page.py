from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from data_classes.product import Product
from typing import List
from utils.logger import allure_log

class HomePage(BasePage):
    PRODUCT_LIST = (By.ID, "tbodyid")  # The container
    PRODUCT_ITEM = (By.CSS_SELECTOR, "div.col-lg-4.col-md-6.mb-4")  # Single product item

    def get_all_products(self):

        # Wait for at least one product to load inside tbodyid
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.PRODUCT_ITEM)
        )
        product_list_element = self.driver.find_element(*self.PRODUCT_LIST)
        products = product_list_element.find_elements(*self.PRODUCT_ITEM)

        if not products:
            allure_log("No products found after waiting")
            return []

        list_of_products: List[Product] = []
        for product in products:
            title = product.find_element(By.CSS_SELECTOR, "h4.card-title a").text
            price = product.find_element(By.TAG_NAME, "h5").text
            description = product.find_element(By.ID, "article").text

            list_of_products.append(Product(title, price, description))

        return list_of_products
