from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from data_classes.product import Product
from typing import List
from utils.logger import allure_log

class HomePage(BasePage):
    PRODUCT_LIST = (By.ID, "tbodyid")  # The container
    PRODUCT_ITEM = (By.CSS_SELECTOR, "div.col-lg-4.col-md-6.mb-4 > div.card") # Single product item
    CARD_ANCHOR =  (By.CSS_SELECTOR, "h4.card-title a")                       # The clickable <a> inside each product

    #Get the list of products -> List[Product]
    def get_all_products(self) -> List[Product]:
        list_of_products: List[Product] = []
        allure_log("get_all_products")

        # Ensure at least one product is visible before proceeding
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PRODUCT_ITEM)
        )

        product_list_element = self.driver.find_element(*self.PRODUCT_LIST)
        products = product_list_element.find_elements(*self.PRODUCT_ITEM)

        if not products:
            allure_log("No products found after waiting")
            return []

        for product in products:
            title = product.find_element(By.CSS_SELECTOR, "h4.card-title a").text
            price = product.find_element(By.TAG_NAME, "h5").text
            description = product.find_element(By.ID, "article").text

            list_of_products.append(Product(title, price, description))

        return list_of_products
    
    #Click on a desired product
    def click_on_product(self, product_title: str):
        
        allure_log("click_on_product")

        # Wait for at least one product to load inside tbodyid
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PRODUCT_ITEM)
        )

        product_list_element = self.driver.find_element(*self.PRODUCT_LIST)
        products = product_list_element.find_elements(*self.PRODUCT_ITEM)
        
        if not products:
            allure_log("No products found after waiting")
        
        #Find the product title, and click on it
        for product in products:
            link_el = product.find_element(*self.CARD_ANCHOR)
            title_text = link_el.text.strip()

            if(title_text.lower() == product_title.lower()):
                
                self.driver.execute_script("arguments[0].scrollIntoView(true);", link_el)
                
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.CARD_ANCHOR)
                )
                link_el.click()
                break
        