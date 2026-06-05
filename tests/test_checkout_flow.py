from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from playwright.sync_api import Page, expect
# for loading variables from .env file
import os
from dotenv import load_dotenv

load_dotenv()

STANDARD_USERNAME = os.getenv("STANDARD_USERNAME")
STANDARD_PASSWORD = os.getenv("STANDARD_PASSWORD")


# TC-03: Full checkout happy process
def test_checkout_happy_path(page: Page):
    LoginPage(page).login(STANDARD_USERNAME, STANDARD_PASSWORD)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    # 0. Remember count of items in cart before adding new product
    initial_count = cart_page.get_cart_count()

    # 1. Add product to cart
    products_page.add_first_product_to_cart()

    # 2. Go to cart and verify count of items increased by 1
    cart_page.go_to_cart()
    expect(cart_page.cart_items).to_have_count(initial_count + 1)

    # 3. Proceed to checkout
    cart_page.proceed_to_checkout()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    # 4. Fill in info
    cart_page.fill_checkout_form("Nastia", "QA Engineer", "02394")
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    # 5. Overview and finish the order
    cart_page.finish_checkout()

    # 6. Verify confirmation message
    expect(cart_page.confirmation_header).to_be_visible()
    expect(cart_page.confirmation_header).to_have_text("Thank you for your order!")

    # 7. Back home
    cart_page.back_home()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")