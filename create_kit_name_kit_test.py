# Импортируем модуль sender_stand_request
import sender_stand_request

# Импортируем модуль data
import data.ру


#Получение Токена
def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    auth_Token = user_response.json()["authToken"]
    return auth_Token


# Смена тела запроса
def get_kit_body(name):
    new_kit_body = data.kit_body.copy()
    new_kit_body['name'] = name
    return new_kit_body


# Функция для позитивной проверки
def positive_assert(kit_body):
    new_kit_body_positive = get_kit_body(kit_body) 
    auth_token = get_new_user_token()
    # Сохраняется результат запроса
    kit_response_positive = sender_stand_request.post_new_client_kit(new_kit_body_positive, auth_token)
    # Проверяется, что код ответа равен 201
    assert kit_response_positive.status_code == 201
    assert new_kit_body_positive["name"] == kit_response_positive.json()["name"]


# Функция для негативной проверки
def negative_assert_code_400(kit_body):
    new_kit_body_negative = get_kit_body(kit_body)
    # в переменную сохраняется результат
    auth_token = get_new_user_token() 
    # сохраняется результат
    kit_response_negative = sender_stand_request.post_new_client_kit(new_kit_body_negative, auth_token)
    # Проверяется, что код ответа равен 400
    assert kit_response_negative.status_code == 400  


# Функция для негативной проверки без имени. Параметр name не передан
def negative_assert_no_name(kit_body):
    auth_token = get_new_user_token()
    kit_response_negative_no_name = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Проверяется, что код ответа равен 400
    assert kit_response_negative_no_name.status_code == 400


# Тест 1. Успешное создание набора. Параметр name состоит из 1 символа
def test_create_kit_1_letter_in_kit_name_get_success_response():
    positive_assert("a")


# Тест 2. Успешное создание набора. Параметр name состоит из 511 символов
def test_create_kit_511_letters_in_kit_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Тест 3. Негативная проверка. Параметр name состоит из 0 символов
def test_create_kit_0_letter_in_kit_name_get_error_response():
    negative_assert_code_400("")


# Тест 4. Негативная проверка. Параметр name состоит из 512 символов
def test_create_kit_512_letters_in_kit_name_get_error_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# Тест 5. Успешное создание набора. Параметр name состоит из английских букв
def test_create_kit_english_letters_in_kit_name_get_success_response():
    positive_assert("QWErty")


# Тест 6. Успешное создание набора. Параметр name состоит из русских букв
def test_create_kit_russian_letters_in_kit_name_get_success_response():
    positive_assert("Мария")


# Тест 7. Успешное создание набора. Параметр name состоит из спецсимволов
def test_create_kit_special_symbols_in_kit_name_get_success_response():
    positive_assert("\"№%@\",")


# Тест 8. Успешное создание набора. Параметр name c пробелами
def test_create_kit_spaces_in_kit_name_get_success_response():
    positive_assert("Человек и КО")


# Тест 9. Успешное создание набора. Парметр name состоит из цифр
def test_create_kit_numbers_in_kit_name_get_success_response():
    positive_assert("123")


# Тест 10. Ошибка. Параметр name не передан
def test_create_kit_no_name_get_error_response():
    # Копируется словарь с телом запроса из файла data в переменную kit_body
    current_kit_body_no_name = data.kit_body.copy()  
    # Удаление параметра name из запроса
    current_kit_body_no_name.pop("name") 
    # Проверка полученного ответа
    negative_assert_no_name(current_kit_body_no_name)

# Тест 11. Ошибка. Параметр name передан типом число
def test_create_kit_type_number_in_kit_name_get_error_response():
    negative_assert_code_400(123)