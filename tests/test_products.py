from utils.logger import allure_log
from pages.home_page import HomePage
from utils.test_data_loader import load_test_data
import pytest

test_data_products = load_test_data('test_data/home_page_test_products.json')

# Testing how many products are on the homepage
@pytest.mark.parametrize("test_case", test_data_products)
def test_show_products_on_homepage(driver, config, test_case):
    allure_log(f"🚀 Test: Show products on homepage started")

    # Expected product titles from JSON
    expected_product_titles = set(test_case["products"])

    driver.get(config["base_url"])

    home_page = HomePage(driver)
    list_of_products = home_page.get_all_products()

    actual_product_titles = set(product.title for product in list_of_products)

    for product in list_of_products:
        allure_log(f"✅ Found product: {product.title}")

    assert len(list_of_products) > 0, "No products found on the homepage!"

    # Compare expected vs actual product titles
    missing_products = expected_product_titles - actual_product_titles
    extra_products = actual_product_titles - expected_product_titles

    assert not missing_products, f" Missing products: {missing_products}"
    assert not extra_products, f" Unexpected extra products: {extra_products}"

    allure_log("Product verification successful!")
