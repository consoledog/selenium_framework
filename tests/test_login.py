from pages.login_page import LoginPage

def test_valid_login(driver, config):
    driver.get(config["base_url"])
    login_page = LoginPage(driver)
    login_page.login(config["username"], config["password"])
    assert login_page.get_text(login_page.WELCOME) == f"Welcome {config["username"]}"

def test_invalid_password_login(driver, config):
    driver.get(config["base_url"])
    login_page = LoginPage(driver)
    login_page.login(config["username2"], config["invalid_password"])
    
    alert = login_page.catch_alert(driver)
    assert alert.text == "Wrong password."
    alert.accept()
