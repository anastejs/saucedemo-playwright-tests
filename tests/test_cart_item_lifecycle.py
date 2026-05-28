import pytest
from pages import products_page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from playwright.sync_api import Page, expect


# TC-04: Verify cart item lifecycle and badge state updates
def test_cart_add_and_remove(page: Page):
    LoginPage(page).login("standard_user", "secret_sauce")
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    # 1. Ensure cart is empty before test
    cart_page.clear_cart()

    # 2.Verify - at least 2 products are available on the page
    item_count = products_page.product_names.count()
    if item_count < 2:
        pytest.fail(f"Not enough products on the page to run the test. Expected at least 2, got {item_count}.")
    
    # 3. Add 2 products and verify - badge shows 2
    products_page.add_products_to_cart(2)
    expect(cart_page.cart_badge).to_have_text("2")

    # 4. Go to cart and verify - 2 items are in the cart
    cart_page.go_to_cart()
    expect(cart_page.cart_items).to_have_count(2)

    # 5. Remove first item and verify - 1 item remains in the cart and badge shows 1
    cart_page.remove_first_item()
    expect(cart_page.cart_items).to_have_count(1)
    expect(cart_page.cart_badge).to_have_text("1")

    # 6. Remove last item and verify cart badge disappears
    cart_page.remove_first_item()
    expect(cart_page.cart_items).to_have_count(0)
    expect(cart_page.cart_badge, "Cart badge should not be visible when cart is empty.").not_to_be_visible()