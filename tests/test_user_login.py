import allure
from api.api_requests import APIRequests
from utils.data_generator import generate_user_data
from utils.expected_data import EXP_DATA


@allure.epic('Test User Authentication')
class TestUserAuthentication:
    api_client = APIRequests()

    @allure.title('Авторизация существующего пользователя')
    def test_login_existing_user(self, create_test_user):
        response = self.api_client.login_user(
            email=create_test_user['email'],
            password=create_test_user['password']
        )
        assert response.status_code == 200
        assert response.json()['success'] is True
        assert 'accessToken' in response.json()

    @allure.title('Авторизация не невалидными данными')
    def test_login_user_with_wrong_credentials(self):
        user_data = generate_user_data()

        wrong_email = 'wrong-' + user_data['email']
        wrong_password = 'wrong-' + user_data['password']
        response = self.api_client.login_user(
            email=wrong_email,
            password=wrong_password
        )
        assert response.status_code == 401
        assert response.json()['success'] is False
        assert response.json()['message'] == EXP_DATA["wrong_credentials"]
