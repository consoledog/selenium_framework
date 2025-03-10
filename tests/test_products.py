from utils.logger import allure_log
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.header_page import HeaderPage
from pages.cart_page import CartPage
from pages.place_order_page import PlaceOrderPage
from pages.thank_you_purchase_page import ThankyouPage
from data_classes.place_order import Placeorder
from utils.test_data_loader import load_test_data
import pytest
import time

test_data_products = load_test_data('test_data/home_page_test_products.json')
cart_data_products = load_test_data('test_data/buy_products_test.json')

# Testing how many products are on the homepage
#@pytest.mark.parametrize("test_case", test_data_products)
@pytest.mark.skip(reason="This test is currently inactive")
def test_show_products_on_homepage(driver, config, test_case):
    allure_log(f"Test: Show products on homepage started")

    home_page = HomePage(driver)
    expected_product_titles = set(test_case["products"])

    driver.get(config["base_url"])

    list_of_products = home_page.get_all_products()
    actual_product_titles = set(product.title for product in list_of_products)

    for product in list_of_products:
        allure_log(f"Found product: {product.title}")

    assert len(list_of_products) > 0, "No products found on the homepage!"

    # Compare expected vs actual product titles
    missing_products = expected_product_titles - actual_product_titles
    extra_products = actual_product_titles - expected_product_titles
    assert not missing_products, f" Missing products: {missing_products}"
    assert not extra_products, f" Unexpected extra products: {extra_products}"

    allure_log("Product verification successful!")


#Put a product in a shopping cart, then buy it
#@pytest.mark.parametrize("test_case", cart_data_products)
@pytest.mark.skip(reason="This test is currently inactive")
def test_buy_products(driver, config, test_case):
    allure_log(f" Test: buy_products")
    
    #Init phase
    home_page = HomePage(driver)
    product_page = ProductPage(driver)
    header_page = HeaderPage(driver)
    cart_page = CartPage(driver)
    place_order_page = PlaceOrderPage(driver)
    thank_you_page = ThankyouPage(driver)

    #Go to website
    driver.get(config["base_url"])

    #Buy a product
    expected_product_titles = set(test_case["products"])
    home_page.click_on_product("Samsung galaxy s6")
    product_page.buy_product()
    alert = product_page.catch_alert(driver)
    allure_log(f"Captured Alert: {alert.text}")
    assert alert.text == "Product added"
    alert.accept()

    #Go to cart
    header_page.click_on_cart()

    #Compare what is in the cart, and what is expected
    list_of_product_titles = set(cart_page.get_all_product_titles())
    allure_log(f"Expected: {expected_product_titles}")
    allure_log(f"Found in cart: {list_of_product_titles}")
    missing_products = expected_product_titles - list_of_product_titles
    extra_products = list_of_product_titles - expected_product_titles
    assert not missing_products, f"Missing products from cart: {missing_products}"
    assert not extra_products, f" Unexpected extra products in cart: {extra_products}"
    allure_log("Product verification in cart successful!")

    #Buy an item from the cart
    cart_page.buy_product()
    place_order = Placeorder("Aleksandar","Serbia","Novi Sad","123123132","02","2025")

    #Fill payment information
    place_order_page.fill_place_order(place_order)
    place_order_page.buy_order()
    
    #Check for the greeting message
    assert thank_you_page.getGreetingMessage() == "Thank you for your purchase!"
    thank_you_page.clickOk()

    time.sleep(5)