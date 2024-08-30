import pytest
from api.api_requests import APIRequests
from utils.data_generator import generate_user_data


@pytest.fixture
def create_test_user():
    api_client = APIRequests()
    user_data = generate_user_data()

    response = api_client.create_user(
        email=user_data['email'],
        password=user_data['password'],
        name=user_data['name']
    )

    yield user_data

    access_token = response.json()['accessToken'].split(' ')[1]
    api_client.delete_user(access_token)


@pytest.fixture
def authorized_token(create_test_user):
    api_client = APIRequests()

    user_data = create_test_user
    auth_response = api_client.login_user(
        email=user_data["email"],
        password=user_data["password"]
    )
    token = auth_response.json()['accessToken'].split(' ')[1]
    return token


@pytest.fixture
def ingredients():
    api_client = APIRequests()

    response = api_client.get_ingredients()
    return [ingredient["_id"] for ingredient in response.json()["data"]]
