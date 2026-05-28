import json
import requests
# import pytest

BASE_URL = "https://reqres.in/api"
API_KEY = "free_user_3EKly1xOLEGiTYzBJl8uknHwczN"
HEADERS = {"x-api-key": API_KEY}

# TC-01: GET list users
def test_get_users():
    response = requests.get(       # send GET request to /users endpoint with page=2
        f"{BASE_URL}/users",
        params={"page": 2},
        headers=HEADERS
    )
    body = response.json()    # parse JSON response -> into python dict 'body' with keys: page, per_page, total, total_pages, data (list of users), support (object)
    data = body["data"]
    # print formatted JSON response for debugging
    # print(json.dumps(body, indent=2))

    # VERIFICATIONS
    assert response.status_code == 200    # verify HTTP status code - 200 OK 
      
    # verify - total number of users
    assert body["total"] == 12, f"Expected total 12, got {body['total']}"

    # verify - last_name of 1. and 2. user
    assert data[0]["last_name"] == "Lawson", f"Expected 'Lawson', got {data[0]['last_name']}"
    assert data[1]["last_name"] == "Ferguson", f"Expected 'Ferguson', got {data[1]['last_name']}"

    # verify - count of users in data matches per_page value (total = 12, per_page = 6)
    total_from_response = body["total"]
    per_page = body["per_page"]
    total_pages = body["total_pages"]
    assert per_page * total_pages == total_from_response, f"Expected {per_page} * {total_pages} = {total_from_response}"

    # verify - data types for each user in data
    for user in data:
        assert isinstance(user["id"], int), f"Expected id to be int, got {type(user['id'])}"
        assert isinstance(user["email"], str), f"Expected email to be str, got {type(user['email'])}"
        assert isinstance(user["first_name"], str), f"Expected first_name to be str, got {type(user['first_name'])}"
        assert isinstance(user["last_name"], str), f"Expected last_name to be str, got {type(user['last_name'])}"
        assert isinstance(user["avatar"], str), f"Expected avatar to be str, got {type(user['avatar'])}"