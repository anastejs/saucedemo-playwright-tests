from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.page.goto("https://www.saucedemo.com/")

        # Find the necessary elements on the page
        self.username_input = self.page.get_by_placeholder("Username")
        self.password_input = self.page.get_by_placeholder("Password")
        self.login_btn = self.page.get_by_role("button", name="Login")
        self.error_message = self.page.locator("[data-test='error']")    # after failed login attempt

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_btn.click()