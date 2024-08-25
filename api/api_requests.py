import requests
import allure
import json
from api.endpoints import Endpoints


class APIRequests:
    BASE_URL = Endpoints.BASE_URL

    def get_ingredients(self):
        endpoint = Endpoints.INGREDIENTS
        with allure.step(f"GET {self.BASE_URL}{endpoint}"):
            response = requests.get(f"{self.BASE_URL}{endpoint}")
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)
            return response

    def create_order(self, ingredients_list, access_token=None):
        endpoint = Endpoints.ORDERS
        with allure.step(f"POST {self.BASE_URL}{endpoint}"):
            headers = {'Authorization': f'Bearer {access_token}'} if access_token else {}
            payload = {'ingredients': ingredients_list}
            response = requests.post(f"{self.BASE_URL}{endpoint}", json=payload, headers=headers)
            allure.attach(json.dumps(payload), name="body", attachment_type=allure.attachment_type.JSON)
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)
            return response

    def create_user(self, email, password, name):
        endpoint = Endpoints.REGISTER
        with allure.step(f"POST {self.BASE_URL}{endpoint}"):
            payload = {'email': email, 'password': password, 'name': name}
            response = requests.post(f"{self.BASE_URL}{endpoint}", json=payload)
            allure.attach(json.dumps(payload), name="body", attachment_type=allure.attachment_type.JSON)
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)
            return response

    def login_user(self, email, password):
        endpoint = Endpoints.LOGIN
        with allure.step(f"POST {self.BASE_URL}{endpoint}"):
            payload = {'email': email, 'password': password}
            response = requests.post(f"{self.BASE_URL}{endpoint}", json=payload)
            allure.attach(json.dumps(payload), name="body", attachment_type=allure.attachment_type.JSON)
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)
            return response

    def get_user_data(self, access_token):
        endpoint = Endpoints.USER
        with allure.step(f"GET {self.BASE_URL}{endpoint}"):
            headers = {'Authorization': f'Bearer {access_token}'}
            response = requests.get(f"{self.BASE_URL}{endpoint}", headers=headers)
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)
            return response

    def update_user_data(self, access_token, email, name):
        endpoint = Endpoints.USER
        with allure.step(f"PATCH {self.BASE_URL}{endpoint}"):
            headers = {'Authorization': f'Bearer {access_token}'}
            payload = {'email': email, 'name': name}
            response = requests.patch(f"{self.BASE_URL}{endpoint}", json=payload, headers=headers)
            allure.attach(json.dumps(payload), name="body", attachment_type=allure.attachment_type.JSON)
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)
            return response

    def delete_user(self, access_token):
        endpoint = Endpoints.USER
        with allure.step(f"DELETE {self.BASE_URL}{endpoint}"):
            headers = {'Authorization': f'Bearer {access_token}'}
            response = requests.delete(f"{self.BASE_URL}{endpoint}", headers=headers)
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)
            return response

    def get_all_orders(self, access_token):
        endpoint = Endpoints.ALL_ORDERS
        with allure.step(f"GET {self.BASE_URL}{endpoint}"):
            headers = {'Authorization': f'Bearer {access_token}'}
            response = requests.get(f"{self.BASE_URL}{endpoint}", headers=headers)
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)
            return response

    def get_user_orders(self, access_token=None):
        endpoint = Endpoints.USER_ORDERS
        with allure.step(f"GET {self.BASE_URL}{endpoint}"):
            headers = {'Authorization': f'Bearer {access_token}'} if access_token else {}
            response = requests.get(f"{self.BASE_URL}{endpoint}", headers=headers)
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)
            return response
