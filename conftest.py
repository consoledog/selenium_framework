import pytest
from utils.driver_factory import get_driver
import yaml
import os
from datetime import datetime

@pytest.fixture(scope="function")
def driver():
    driver = get_driver("chrome")
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def config():
    with open("config/config.yaml") as file:
        return yaml.safe_load(file)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver")
        if driver:
            timestamp =  datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            file_name = f"{test_name}_{timestamp}.png"
            file_path = os.path.join(screenshot_dir, file_name)
            driver.save_screenshot(file_path)
            print(f"\n📸 Screenshot saved: {file_path}")