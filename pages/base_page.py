from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    def type(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)
    
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
    def catch_alert(self, driver, timeout=10):
        try:
            WebDriverWait(driver, timeout).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            return alert
        except TimeoutException:
            print("No alert appeared within the timeout.")
            return None