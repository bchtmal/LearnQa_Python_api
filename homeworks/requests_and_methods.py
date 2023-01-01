import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
prob = 40*"-"

# -----------------------------------------------------------------------
response1 = requests.post(url)
print("Тест-1")
print(response1.text)
print(response1.status_code)

# -----------------------------------------------------------------------
response2 = requests.head(url, params={"method": "HEAD"})
print("Тест-2")
print(response2.text)
print(response2.status_code)

# ------------------------------------------------------------------------
response3 = requests.get(url, params={"method": "GET"})
print("Тест-3")
print(response3.text)
print(response3.status_code)

# ------------------------------------------------------------------------
print("Скрипт-4", end='\n\n')
methods = ["POST", "GET", "PUT", "DELETE"]
for id in methods:

    get_response = requests.get(url, params={'method': f"{id}"})
    print("GET request")
    print(f"{id} method parameter")
    print(f"Response code: {get_response.status_code}")
    print(f"Response text: {get_response.text}", end='\n\n')
    print(prob)

    post_response = requests.post(url, data={'method': f"{id}"})
    print("POST request")
    print(f"{id} method parameter")
    print(f"Response code: {post_response.status_code}")
    print(f"Response text: {post_response.text}", end='\n\n')
    print(prob)

    put_response = requests.put(url, data={'method': f"{id}"})
    print(f"PUT request")
    print(f"{id} method parameter")
    print(f"Response code: {put_response.status_code}")
    print(f"Response text: {put_response.text}", end='\n\n')
    print(prob)

    delete_response = requests.delete(url, data={'method': f"{id}"})
    print(f"DELETE request")
    print(f"{id} method parameter")
    print(f"Response code: {delete_response.status_code}")
    print(f"Response text: {delete_response.text}", end='\n')
    print(prob)


