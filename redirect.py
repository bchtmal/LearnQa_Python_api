import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

history = response.history

print(history)
print(response.url)