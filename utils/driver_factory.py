from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tempfile

def get_driver(browser_name="chrome"):
    if browser_name == "chrome":
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--window-size=1920,1080")
        options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")
        return webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception(f"Browser '{browser_name}' is not supported")
    driver.maximize_window()
    return driver
