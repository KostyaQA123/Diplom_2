# Дипломный проект. Задание 2: API-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

Основа для написания автотестов — фреймворк pytest

## Реализованные сценарии

### TestUserCreation
* test_create_unique_user — Создание уникального пользователя
* test_create_existing_user — Создание существующего пользователя
* test_create_user_with_missing_field — Создание пользователя без обязательных параметров

### TestUserAuthentication
* test_login_existing_user — Авторизация существующего пользователя'
* test_login_user_with_wrong_credentials — Авторизация не невалидными данными

### TestUserUpdate
* test_update_user_with_authorization — Обновление данных авторизованного пользователя
* test_update_user_without_authorization — Обновление данных неавторизованного пользователя

### TestOrderCreation
* test_create_order_with_authorization — Создание заказа авторизованным пользователем
* test_create_order_without_authorization — Создание заказа неавторизованным пользователем
* test_create_order_with_one_ingredient — Создание заказа c 1 ингредиентом'
* test_create_order_without_ingredients — Создание заказа без ингредиентов
* test_create_order_with_invalid_ingredients — Создание заказа с некорректным ингредиентом

### TestUserOrders
* test_get_orders_for_authorized_user — Получение заказов авторизованного пользователя
* test_get_orders_for_unauthorized_user — Получение заказов без авторизации

## Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание Allure-отчета**

>  `pytest -v tests/ --alluredir=allure_results`

**Посмотреть отчёт о тестировании**

>  `allure serve allure_results`