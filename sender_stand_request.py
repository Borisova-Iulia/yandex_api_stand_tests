# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data 



# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH, 
        json=body,
        headers=data.headers
    )
    if response.status_code != 200:
        print(f"Error creating user: {response.status_code} - {response.text}")
    return response

# Получение авторизационного токена
def get_auth_token():
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        headers=data.headers
    )
    if response.status_code != 200:
        print(f"Error getting auth token: {response.status_code} - {response.text}")
        return None  
    return response.json().get('token') 

# Создание нового набора
def post_new_client_kit(kit_body, auth_token):
    headers = data.headers.copy()
    headers["Authorization"] = "Bearer " + auth_token
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_PRODUCTS_KIT_PATH,
        json=kit_body,
        headers=headers
    )
    if response.status_code != 200:
        print(f"Error creating client kit: {response.status_code} - {response.text}")
    return response