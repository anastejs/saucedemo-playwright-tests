# Test Cases

## UI Tests — [saucedemo.com](https://www.saucedemo.com/)

### TC-01 Login Functionality

**TC-01a**: Successful Login

Precondition:
- User is on the login page
- User has valid credentials

| Step | Expected Result |
|---|---|
| 1. Enter valid username and password | Input fields contain entered values |
| 2. Click Login button | Redirected to `/inventory.html` |

**TC-01b**: Locked Out User

Precondition:
- User is on the login page
- User account is locked

| Step | Expected Result |
|---|---|
| 1. Enter locked user credentials | Input fields contain entered values |
| 2. Click Login button | Error message is visible: "Sorry, this user has been locked out" |

**TC-01c**: Failed Login with Invalid Password

Precondition:
- User is on the login page
- User has a valid username and an invalid password

| Step | Expected Result |
|---|---|
| 1. Enter valid username and invalid password | Input fields contain entered values |
| 2. Click Login button | Error message is visible: "Epic sadface: Username and password do not match any user in this service" |

### TC-02 Product Sorting

Precondition:
- User is logged in
- User is on the inventory page
- At least 3 products are visible

| Step | Expected Result |
|---|---|
| 1. Select "Name (A to Z)" from sort dropdown | Products sorted alphabetically ascending |
| 2. Select "Name (Z to A)" from sort dropdown | Products sorted alphabetically descending |
| 3. Select "Price (low to high)" from sort dropdown | Products sorted by price ascending |
| 4. Select "Price (high to low)" from sort dropdown | Products sorted by price descending |

### TC-03 Checkout Flow (happy path)

Precondition:
- User is logged in
- At least 1 product is available in the inventory

| Step | Expected Result |
|---|---|
| 1. Add a product to cart | Cart badge count increases by 1 |
| 2. Go to cart | Cart contains the added item |
| 3. Click "Checkout" | Redirected to `/checkout-step-one.html` |
| 4. Fill in first name, last name, postal code | Form is filled |
| 5. Click "Continue" | Redirected to `/checkout-step-two.html` |
| 6. Click "Finish" | Confirmation message "Thank you for your order!" is visible |
| 7. Click "Back Home" | Redirected to `/inventory.html` |

### TC-04 Cart Item Lifecycle

Precondition:
- User is logged in
- Cart is empty (cleared automatically before test)
- At least 2 products are available in the inventory

| Step | Expected Result |
|---|---|
| 1. Add 2 products to cart | Cart badge shows "2" |
| 2. Go to cart | 2 items are present in the cart |
| 3. Remove first item | Cart badge shows "1", 1 item remains |
| 4. Remove last item | Cart badge is not visible, cart is empty |

---

## API Tests — [reqres.in](https://reqres.in/)

### TC-05 GET /users — List Users

Precondition:
- Valid API key is available
- API key is set in request headers

| Step | Expected Result |
|---|---|
| 1. Send `GET /api/users?page=2` | Status code is `200 OK` |
| 2. Check `total` number of users | Value equals `12` |
| 3. Check last_name values of users at indexes 0 and 1 | Values are "Lawson" and "Ferguson" respectively |
| 4. Check `len(data)` vs `per_page` | Number of returned users matches `per_page` value |
| 5. Check pagination: `ceil(total / per_page)` | Result equals `total_pages` |
| 6. Verify response field data types | `id` (int), `email` (str), `first_name` (str), `last_name` (str), `avatar` (str) |

### TC-06 POST /users — Create User

Precondition:
- Valid API key is available
- API key is set in request headers
- Test data with `name` and `job` fields is loaded from `users.json`

| Step | Expected Result |
|---|---|
| 1. Send `POST /api/users` with `name` and `job` | Status code is `201 Created` |
| 2. Check response body contains `id` | Field `id` is present |
| 3. Check response body contains `createdAt` | Field `createdAt` is present and has valid ISO 8601 format |
| 4. Check response time | Response is received within 2 seconds |
| 5. Check response schema | `id` (str), `name` (str), `job` (str), `createdAt` (str) |