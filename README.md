# saucedemo-playwright-tests

![Python](https://img.shields.io/badge/Python-3.13-B5D5F5?style=flat&logo=python&logoColor=555555)
![Playwright](https://img.shields.io/badge/Playwright-1.60-B5F5D5?style=flat&logo=playwright&logoColor=555555)
![pytest](https://img.shields.io/badge/pytest-9.0.3-F5D5B5?style=flat&logo=pytest&logoColor=555555)
![requests](https://img.shields.io/badge/requests-2.34.2-F5B5D5?style=flat&logo=python&logoColor=555555)
![python-dotenv](https://img.shields.io/badge/python--dotenv-1.2.2-F5F5B5?style=flat&logo=dotenv&logoColor=555555)
![pytest-html](https://img.shields.io/badge/pytest--html-4.2.0-D5B5F5?style=flat&logo=pytest&logoColor=555555)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-B5D5F5?style=flat&logo=githubactions&logoColor=555555)
![POM](https://img.shields.io/badge/Pattern-Page_Object_Model-D5F5B5?style=flat&logoColor=555555)
![Data-Driven](https://img.shields.io/badge/Pattern-Data_Driven-F5D5F5?style=flat&logoColor=555555)

Python-based test automation framework for [saucedemo.com](https://www.saucedemo.com/) (UI) and [reqres.in](https://reqres.in/) (API) built with Python, Pytest and Playwright.

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
├── TEST_CASES.md           # structured test case documentation
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
