import requests
import allure
import json
from api.endpoints import Endpoints


class APIRequests:
    BASE_URL = Endpoints.BASE_URL

    @allure.step("Получение списка ингредиентов")
    def get_ingredients(self):
        response = requests.get(f"{self.BASE_URL}{Endpoints.INGREDIENTS}")
        return response

    @allure.step("Создание заказа")
    def create_order(self, ingredients_list, access_token=None):
        headers = {'Authorization': f'Bearer {access_token}'} if access_token else {}
        payload = {'ingredients': ingredients_list}
        response = requests.post(f"{self.BASE_URL}{Endpoints.ORDERS}", json=payload, headers=headers)
        return response

    @allure.step("Создание пользователя")
    def create_user(self, email, password, name):
        payload = {'email': email, 'password': password, 'name': name}
        response = requests.post(f"{self.BASE_URL}{Endpoints.REGISTER}", json=payload)
        return response

    @allure.step("Авторизация пользователя")
    def login_user(self, email, password):
        payload = {'email': email, 'password': password}
        response = requests.post(f"{self.BASE_URL}{Endpoints.LOGIN}", json=payload)
        return response

    @allure.step("Получение данных пользователя")
    def get_user_data(self, access_token):
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get(f"{self.BASE_URL}{Endpoints.USER}", headers=headers)
        return response

    @allure.step("Обновление данных пользователя")
    def update_user_data(self, access_token, email, name):
        headers = {'Authorization': f'Bearer {access_token}'}
        payload = {'email': email, 'name': name}
        response = requests.patch(f"{self.BASE_URL}{Endpoints.USER}", json=payload, headers=headers)
        return response

    @allure.step("Удаление пользователя")
    def delete_user(self, access_token):
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.delete(f"{self.BASE_URL}{Endpoints.USER}", headers=headers)
        return response

    @allure.step("Получение заказов")
    def get_all_orders(self, access_token):
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get(f"{self.BASE_URL}{Endpoints.ALL_ORDERS}", headers=headers)
        return response

    @allure.step("Получение заказов пользователя")
    def get_user_orders(self, access_token=None):
        headers = {'Authorization': f'Bearer {access_token}'} if access_token else {}
        response = requests.get(f"{self.BASE_URL}{Endpoints.USER_ORDERS}", headers=headers)
        return response
