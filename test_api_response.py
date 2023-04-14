import requests
import pytest

# API URL to be Tested
API_URL = "https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals"

# fixture that will return instance of requests and session


@pytest.fixture
def api_client():
    return requests.Session()

# function to check response code


def test_api_response_code(api_client):
    response = api_client.get(API_URL)

    try:
        assert response.status_code == 200
    except AssertionError:
        print(f"Received a response with status code {response.status_code}")

# function to check null values if present in 'name' and 'bands'


def test_api_null_values(api_client):
    response = api_client.get(API_URL)
    data = response.json()

    try:
        if isinstance(data, dict):
            assert data["name"] is not None
            assert data["bands"] is not None
            for band in data["bands"]:
                assert band["name"] is not None
                assert band["recordLabel"] is not None
        elif isinstance(data, list):
            for festival in data:
                assert festival["name"] is not None
                assert festival["bands"] is not None
                for band in festival["bands"]:
                    assert band["name"] is not None
                    assert band["recordLabel"] is not None
    except KeyError:
        pytest.fail("Expected keys not found")
