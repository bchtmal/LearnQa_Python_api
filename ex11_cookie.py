import requests

def test_request_cookie():
    resp = requests.get("https://playground.learnqa.ru/api/homework_cookie")
    assert resp.cookies.get("HomeWork") == "hw_value"