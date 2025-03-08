from pages.login_page import LoginPage
from utils.test_data_loader import load_test_data
from utils.data_faker import DataGenerator
from utils.logger import allure_log
import pytest

# Load data from JSON
test_data_valid = load_test_data('test_data/login_test_data_valid.json')
test_data_invalid = load_test_data('test_data/login_test_data_invalid.json')

@pytest.mark.parametrize("credentials", test_data_valid)
def test_valid_login(driver, config, credentials):
    username = credentials["username"]
    password = credentials["password"]
    allure_log(f"🚀 Test Started for {username} and {password}")

    driver.get(config["base_url"])
    allure_log("Navigated to login page")

    login_page = LoginPage(driver)
    login_page.login(username, password)
    allure_log("Clicked Login Button")

    allure_log("Check for the Welcome text")
    assert login_page.get_text(login_page.WELCOME) == f"Welcome {username}"

@pytest.mark.parametrize("credentials", test_data_invalid)
def test_invalid_password_login(driver, config, credentials):
    username = credentials["username"]
    password = credentials["password"]
    allure_log(f"🚀 Test Started for {username} and {password}")

    driver.get(config["base_url"])
    allure_log("Navigated to login page")

    login_page = LoginPage(driver)
    login_page.login(username, password)
    allure_log("Clicked Login Button")
    
    alert = login_page.catch_alert(driver)
    allure_log(f"Captured Alert: {alert.text}")
    
    assert alert.text == "Wrong password."
    alert.accept()

#Example of how to use data faker
#@pytest.mark.parametrize("user_data", [data_gen.generate_user() for _ in range(3)])  # Generates 3 unique users
#def test_login_with_fake_data(driver, config, user_data):
#    driver.get(config["base_url"])
#    login_page = LoginPage(driver)
#    
#    print(f"Testing login with: {user_data['username']} | {user_data['email']} | {user_data['password']}")
#    
#    login_page.login(user_data["username"], user_data["password"])

    # Example assertion (modify as per actual expected behavior)
#    assert login_page.get_error_message() == "Invalid username or password."
