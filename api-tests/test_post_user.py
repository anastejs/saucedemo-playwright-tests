import requests
from pathlib import Path
import json
# for loading variables from .env file
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://reqres.in/api"
API_KEY = os.getenv("API_KEY")
HEADERS = {"x-api-key": API_KEY}
RESPONSE_TIME_LIMIT_MS = 2000  # 2 seconds — realistic limit for public API
# 100ms - from the task, but for a public API over the Internet, the real limit is more


def load_test_data():
    file_path = Path(__file__).parent.parent / "test_data" / "users.json"
    with open(file_path) as f:
        return json.load(f)

# TC-2: POST create user
def test_post_create_user():
    users = load_test_data()

    for user in users:
        response = requests.post(
            f"{BASE_URL}/users",
            json=user,
            headers=HEADERS
        )
        body = response.json()    # JSON response -> python dict
        # print formatted JSON response for debugging
        print(json.dumps(body, indent=2))

        # VERIFICATIONS
        assert response.status_code == 201, f"Expected status 201, got {response.status_code}"

        # verify - response contains id
        assert "id" in body, f"Expected 'id' in response, got {body}"

        # verify - response contains createdAt timestamp
        assert "createdAt" in body, f"Expected 'createdAt' in response, got {body}"

        # verify - response time
        response_time_ms = response.elapsed.total_seconds() * 1000
        assert response_time_ms < RESPONSE_TIME_LIMIT_MS, (f"Response time exceeded limit: {response_time_ms:.2f}ms")

        # verify - response schema (verify data types)
        assert isinstance(body["id"], str), f"Expected id to be str, got {type(body['id'])}"
        assert isinstance(body["name"], str), f"Expected name to be str, got {type(body['name'])}"
        assert isinstance(body["job"], str), f"Expected job to be str, got {type(body['job'])}"
        assert isinstance(body["createdAt"], str), f"Expected createdAt to be str, got {type(body['createdAt'])}"