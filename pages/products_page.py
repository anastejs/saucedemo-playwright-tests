from playwright.sync_api import Page


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page
        # Find the necessary elements
        self.sort_dropdown = self.page.locator("[data-test='product-sort-container']")
        self.product_names = self.page.locator("[data-test='inventory-item-name']")
        self.product_prices = self.page.locator("[data-test='inventory-item-price']")

    def sort_by(self, option: str):
        self.sort_dropdown.select_option(option)    # a-z, z-a, low-high($), high-low($)

    def get_product_names(self) -> list[str]:
        return self.product_names.all_inner_texts()

    def get_product_prices(self) -> list[float]:
            prices = self.product_prices.all_inner_texts()
            return [float(p.replace("$", "")) for p in prices]
    
    # for test_checkout_flow test case
    def add_first_product_to_cart(self):
        self.page.locator("[data-test='add-to-cart-sauce-labs-backpack']").first.click()

    # Add specified number of products to cart
    # что если count больше количества товаров на странице? - будет ошибка, так и должно быть, так как тест должен знать о 
    def add_products_to_cart(self, count: int):
        buttons = self.page.get_by_role("button", name="add to cart")
        for i in range(count):
            buttons.nth(i).click()