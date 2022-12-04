import requests

# print('Hello from Alex') # первое задание

response = requests.get('https://playground.learnqa.ru/api/get_text')
print(response.text)