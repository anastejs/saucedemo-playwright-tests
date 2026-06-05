# saucedemo-playwright-tests

Automated test suite for [saucedemo.com](https://www.saucedemo.com/) (UI) and [reqres.in](https://reqres.in/) (API)

## 📁 Project Structure

```
saucedemo-playwright-tests/
├── .github/
│   └── workflows/
│       └── test.yml        # CI pipeline configuration
├── api-tests/
│   ├── test_get_users.py   
│   └── test_post_user.py 
├── pages/                 
│   ├── cart_page.py
│   ├── login_page.py
│   └── products_page.py
├── test_data/
│   └── users.json          # test data for POST /users  
├── tests/                  # UI tests
│   ├── test_cart_item_lifecycle.py
│   ├── test_checkout_flow.py
│   ├── test_login.py
│   └── test_sorting_products.py
├── .env.example            # environment variables template
├── .gitignore
├── pytest.ini
└── requirements.txt
```


## Installation

```bash
# Clone the repository
git clone https://github.com/anastejs/saucedemo-playwright-tests.git
cd saucedemo-playwright-tests

# Create and activate virtual environment
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass    # (optional) I needed this
venv\Scripts\activate       

# Install dependencies
pip install -r requirements.txt
playwright install
```

## Configuration

Add your API key from [app.reqres.in](https://app.reqres.in/api-keys) to:
- `.env` → `API_KEY = ...`

## Running Tests (locally)

```bash
# All tests
pytest

# UI tests only
pytest tests/

# API tests only
pytest api-tests/ -v

# Specific test file
pytest tests/test_checkout_flow.py
```

## Test Report

Generate a local report after running tests:

```bash
pytest --html=test-results/report.html --self-contained-html
```
Open `report.html` in browser to view results.