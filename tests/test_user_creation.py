import pytest
import allure
from api.api_requests import APIRequests
from utils.data_generator import generate_user_data
from utils.expected_data import EXP_DATA


@allure.epic('Test User Creation')
class TestUserCreation:
    api_client = APIRequests()

    @allure.title('Создание уникального пользователя')
    def test_create_unique_user(self):
        user_data = generate_user_data()

        response = self.api_client.create_user(
            email=user_data['email'],
            password=user_data['password'],
            name=user_data['name']
        )
        assert response.status_code == 200
        assert response.json()['success'] is True
        assert 'accessToken' in response.json()

    @allure.title('Создание существующего пользователя')
    def test_create_existing_user(self):
        user_data = generate_user_data()

        response = self.api_client.create_user(
            email=user_data['email'],
            password=user_data['password'],
            name=user_data['name']
        )
        assert response.json()['success'] is True

        response = self.api_client.create_user(
            email=user_data['email'],
            password=user_data['password'],
            name=user_data['name']
        )
        assert response.status_code == 403
        assert response.json()['success'] is False
        assert response.json()['message'] == EXP_DATA["user_exists"]

    @allure.title('Создание пользователя без обязательных параметров')
    @pytest.mark.parametrize("field", ["email", "password", "name"])
    def test_create_user_with_missing_field(self, field):
        user_data = generate_user_data()

        incomplete_user_data = user_data.copy()
        incomplete_user_data.pop(field, None)

        response = self.api_client.create_user(
            email=incomplete_user_data.get("email"),
            password=incomplete_user_data.get("password"),
            name=incomplete_user_data.get("name")
        )
        assert response.status_code == 403
        assert response.json()['success'] is False
        assert field in response.json()['message'].lower()
