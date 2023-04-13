import requests
import pytest

API_URL = "https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals"


@pytest.fixture
def api_client():
    return requests.Session()


def test_api_response_code(api_client):
    response = api_client.get(API_URL)

    assert response.status_code == 200


def test_api_null_values(api_client):
    response = api_client.get(API_URL)
    data = response.json()

    try:
        if isinstance(data, dict):
            assert data["name"] is not None
            assert data["bands"] is not None
        elif isinstance(data, list):
            for item in data:
                assert item["name"] is not None
                assert item["bands"] is not None
    except KeyError:
        pytest.fail("Expected keys not found")
