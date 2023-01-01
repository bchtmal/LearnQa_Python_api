import requests


def test_secret_header():
    get_header_url = "https://playground.learnqa.ru/api/homework_header"
    get_homework_header_response = requests.get(get_header_url)
    secret_header = get_homework_header_response.headers.get("x-secret-homework-header")

    assert secret_header == "Some secret value"