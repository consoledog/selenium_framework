from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List

class CartPage(BasePage):
    PRODUCT_TABLE = (By.ID, "tbodyid")
    PRODUCT_ROWS = (By.XPATH, "//tbody/tr")
    PLACE_ORDER = (By.XPATH, "//button[contains(text(),'Place Order')]")

    def get_all_product_titles(self) -> List[str]:
        # Wait until at least one row is present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.PRODUCT_ROWS)
        )

        # Find all product rows dynamically
        product_list_element = self.driver.find_element(*self.PRODUCT_TABLE)
        products = product_list_element.find_elements(*self.PRODUCT_ROWS)

        list_of_products: List[str] = []

        for product in products:
            try:
                title = product.find_element(By.XPATH, ".//td[2]").text
                list_of_products.append(title)
            except:
                print("Could not extract product title for a row!")

        return list_of_products
    
    def buy_product(self):
        self.click(self.PLACE_ORDER)
