import pytest
from utils.driver_factory import get_driver
import yaml

@pytest.fixture(scope="function")
def driver():
    driver = get_driver("chrome")
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def config():
    with open("config/config.yaml") as file:
        return yaml.safe_load(file)
