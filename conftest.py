import pytest
from utils.driver_factory import get_driver
import yaml
import os
from datetime import datetime
import glob

@pytest.fixture(params=["chrome", "firefox"], scope="function") #params=["chrome", "firefox"]]
def driver(request):
    driver = get_driver(request.param)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def config():
    with open("config/config.yaml") as file:
        return yaml.safe_load(file)

# Function to make screenshot on test fail
#item: The test case currently being executed.
#call: Information about the test execution, including its result.
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    
    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver")
        if driver:
            # Define screenshot directory
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            
            # Remove old screenshots before saving new ones
            if os.path.exists(screenshot_dir):
                for file in glob.glob(os.path.join(screenshot_dir, "*.png")):
                    os.remove(file)
            
            # Ensure directory exists
            os.makedirs(screenshot_dir, exist_ok=True)

            # Generate new screenshot file name
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name
            file_name = f"{test_name}_{timestamp}.png"
            file_path = os.path.join(screenshot_dir, file_name)

            # Save the screenshot
            driver.save_screenshot(file_path)
            print(f"\nScreenshot saved: {file_path}")
