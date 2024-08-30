import allure
from api.api_requests import APIRequests
from utils.expected_data import EXP_DATA


@allure.epic('Test Order Creation')
class TestUserOrders:
    api_client = APIRequests()

    @allure.title('Получение заказов авторизованного пользователя')
    def test_get_orders_for_authorized_user(self, authorized_token):
        response = self.api_client.get_user_orders(access_token=authorized_token)
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert isinstance(response.json()["orders"], list)

    @allure.title('Получение заказов без авторизации')
    def test_get_orders_for_unauthorized_user(self):
        response = self.api_client.get_user_orders()
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == EXP_DATA["no_auth"]
