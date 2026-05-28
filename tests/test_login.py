from pages.login_page import LoginPage
from playwright.sync_api import Page, expect

# could be done with
# @pytest.mark.parametrize("username, password, expected_url, expected_error", [...])

# TC-01a: Successful login
def test_successful_login(page: Page):
    username = "standard_user"
    password = "secret_sauce"
    login_page = LoginPage(page)
    login_page.login(username, password)

    # verify - the URL should be "https://www.saucedemo.com/inventory.html" after successful login
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

# TC-01b: Locked out user sees an error message
def test_locked_out_user(page: Page):
    username = "locked_out_user"
    password = "secret_sauce"
    login_page = LoginPage(page)
    login_page.login(username, password)

    # verify - the error message should be visible and contain text "Sorry, this user has been locked out"
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Sorry, this user has been locked out")

# TC-01c: Failed login
def test_failed_login(page: Page):
    username = "standard_user"
    password = "yapayapa"
    login_page = LoginPage(page)
    login_page.login(username, password)

    # verify - the error message should be visible and have specific text
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text("Epic sadface: Username and password do not match any user in this service")
