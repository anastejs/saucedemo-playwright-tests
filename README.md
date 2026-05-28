# saucedemo-playwright-tests

Automated tests for [saucedemo.com](https://www.saucedemo.com/) (UI) and [reqres.in](https://reqres.in/) (API)

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
- `api-tests/test_get_users.py` → `API_KEY = "..."`
- `api-tests/test_post_user.py` → `API_KEY = "..."`

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
