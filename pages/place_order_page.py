from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from data_classes.place_order import Placeorder

class PlaceOrderPage(BasePage):
    NAME = (By.ID, "name")
    COUNTRY = (By.ID, "country")
    CITY = (By.ID, "city")
    CREDIT_CARD = (By.ID, "card")
    MONTH = (By.ID, "month")
    YEAR = (By.ID, "year")
    PURCHASE_BUTTON = (By.XPATH, "//button[contains(text(),'Purchase')]")
    CANCEL_BUTTON = (By.XPATH, "//body/div[@id='orderModal']/div[1]/div[1]/div[3]/button[1]")

    def fill_place_order(self, place_order: Placeorder):
        self.type(self.NAME,place_order.name)
        self.type(self.COUNTRY,place_order.country)
        self.type(self.CITY,place_order.city)
        self.type(self.CREDIT_CARD,place_order.credit_card)
        self.type(self.MONTH,place_order.month)
        self.type(self.YEAR,place_order.year)
    
    def buy_order(self):
        self.click(self.PURCHASE_BUTTON)


    