import pytest
from api.api_requests import APIRequests
from utils.data_generator import get_user_data


@pytest.fixture
def api_client():
    return APIRequests()


@pytest.fixture
def user_data():
    return get_user_data()


@pytest.fixture
def create_test_user(api_client, user_data):
    response = api_client.create_user(
        email=user_data['email'],
        password=user_data['password'],
        name=user_data['name']
    )

    yield user_data

    access_token = response.json()['accessToken'].split(' ')[1]
    api_client.delete_user(access_token)


@pytest.fixture
def authorized_token(api_client, create_test_user):
    user_data = create_test_user
    auth_response = api_client.login_user(
        email=user_data["email"],
        password=user_data["password"]
    )
    token = auth_response.json()['accessToken'].split(' ')[1]
    return token


@pytest.fixture
def ingredients(api_client):
    response = api_client.get_ingredients()
    return [ingredient["_id"] for ingredient in response.json()["data"]]
