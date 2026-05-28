from pages.login_page import LoginPage          # for login functionality
from pages.products_page import ProductsPage
from playwright.sync_api import Page, expect
import pytest    # for feature-based test parametrization

@pytest.fixture
def login(page: Page):
    LoginPage(page).login("standard_user", "secret_sauce")
    return page

# TC-02: Product sorting functionality
@pytest.mark.parametrize("sort_option, sort_key, reverse", [
    ("az", "name", False),   # A to Z
    ("za", "name", True),    # Z to A
    ("lohi", "price", False),   # price low to high
    ("hilo", "price", True),    # price high to low
])

def test_product_sorting(login: Page, sort_option, sort_key, reverse):
    products_page = ProductsPage(login)
     # verify - sort dropdown is visible and can be used
    expect(products_page.sort_dropdown).to_be_visible()
    products_page.sort_by(sort_option)

    if sort_key == "name":
        items = products_page.get_product_names()
    else:
        items = products_page.get_product_prices()

    expected_list = sorted(items, reverse=reverse)

    # verify - the list of items should be correctly sorted, not using expect() due to list sorting complexity
    assert items == expected_list, (
        f"Sorting failed for '{sort_option}'.\n"
        f"Expected: {expected_list}\n"
        f"Actual:   {items}")