import allure
from api.api_requests import APIRequests


@allure.epic('Test Order Creation')
class TestOrderCreation:
    api_client = APIRequests()

    @allure.title('Создание заказа авторизованным пользователем')
    def test_create_order_with_authorization(self, authorized_token, ingredients):
        response = self.api_client.create_order(ingredients_list=ingredients, access_token=authorized_token)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Создание заказа неавторизованным пользователем')
    def test_create_order_without_authorization(self, ingredients):
        response = self.api_client.create_order(ingredients_list=ingredients)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Создание заказа c 1 ингредиентом')
    def test_create_order_with_one_ingredient(self, authorized_token, ingredients):
        ingredient_subset = ingredients[:1]
        response = self.api_client.create_order(ingredients_list=ingredient_subset, access_token=authorized_token)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self, authorized_token):
        response = self.api_client.create_order(ingredients_list=[], access_token=authorized_token)
        assert response.status_code == 400
        assert response.json()["success"] is False

    @allure.title('Создание заказа с некорректным ингредиентом')
    def test_create_order_with_invalid_ingredients(self, authorized_token):
        invalid_ingredients = ["no_existing_ingredient"]
        response = self.api_client.create_order(ingredients_list=invalid_ingredients, access_token=authorized_token)
        assert response.status_code == 500
