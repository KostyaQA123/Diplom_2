import allure
from api.api_requests import APIRequests
from utils.data_generator import get_user_data
from utils.expected_data import EXP_DATA


@allure.epic('Test User Update')
class TestUserUpdate:
    api_client = APIRequests()

    @allure.title('Обновление данных авторизованного пользователя')
    def test_update_user_with_authorization(self, authorized_token):
        updated_data = get_user_data()
        response = self.api_client.update_user_data(
            access_token=authorized_token,
            email=updated_data['email'],
            name=updated_data['name']
        )
        assert response.status_code == 200
        assert response.json()['success'] is True
        assert response.json()['user']['email'] == updated_data['email']
        assert response.json()['user']['name'] == updated_data['name']

    @allure.title('Обновление данных неавторизованного пользователя')
    def test_update_user_without_authorization(self):
        updated_data = get_user_data()
        response = self.api_client.update_user_data(
            access_token="",
            email=updated_data['email'],
            name=updated_data['name']
        )
        assert response.status_code == 401
        assert response.json()['success'] is False
        assert response.json()['message'] == EXP_DATA["no_auth"]
