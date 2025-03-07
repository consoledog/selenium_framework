from pages.login_page import LoginPage

def test_valid_login(driver, config):
    driver.get(config["base_url"])
    login_page = LoginPage(driver)
    login_page.login(config["username"], config["password"])