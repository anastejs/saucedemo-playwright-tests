from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page

        # "Your cart" page - find the necessary elements
        self.cart_icon = self.page.locator("[data-test='shopping-cart-link']")
        self.checkout_btn = self.page.get_by_role("button", name="Checkout")   # Checkout
        self.cart_items = self.page.locator("[data-test='inventory-item']")
        self.cart_badge = self.page.locator("[data-test='shopping-cart-badge']")

        # Checkout: Your Information - find the necessary elements
        self.first_name = self.page.locator("[data-test='firstName']")
        self.last_name = self.page.locator("[data-test='lastName']")
        self.zip_code = self.page.locator("[data-test='postalCode']")
        self.continue_btn = self.page.locator("[data-test='continue']")    # Continue

        # Checkout: Overview - find the necessary elements
        self.finish_btn = self.page.locator("[data-test='finish']")    # Finish

        # Checkout: Complete
        self.confirmation_header = self.page.locator("[data-test='complete-header']")   # Thank you for your order!

    def go_to_cart(self):
        self.cart_icon.click()

    # Get count of items in the cart
    def get_cart_count(self) -> int:
        if self.cart_badge.is_visible():
            return int(self.cart_badge.text_content())
        return 0

    def proceed_to_checkout(self):
        self.checkout_btn.click()

    def fill_checkout_form(self, first_name: str, last_name: str, zip_code: str):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.zip_code.fill(zip_code)
        self.continue_btn.click()

    def finish_checkout(self):
        self.finish_btn.click()

    def back_home(self):
        self.page.get_by_role("button", name="Back Home").click()

    # Not used, but may be useful in the future (yeap)
    # Navigate to cart and remove all items if any exist
    def clear_cart(self):
        self.cart_icon.click()
        remove_buttons = self.page.locator("[data-test^='remove']")
        while remove_buttons.count() > 0:
            remove_buttons.first.click()
        self.page.go_back()

    def remove_first_item(self):
        self.page.locator("[data-test^='remove']").first.click()

    def is_cart_badge_visible(self) -> bool:
        return self.cart_badge.is_visible()