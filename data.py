# заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
headers = {
    "Content-Type": "application/json"
}

# данные пользователя для создания новой записи пользователя в системе
# содержат имя, телефон и адрес пользователя

user_body = {
    "firstName": "Юлия", # Имя пользователя
    "phone": "+79531645357", # Контактный телефон пользователя
    "address": "г. Санкт-Петербург, ул. Среднерогатская, д. 16" # Адрес пользователя
}

kit_body = {
    "name": "Клубок продуктов"
}