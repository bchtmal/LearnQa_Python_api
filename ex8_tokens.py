import json
import time


import requests

url = "https://playground.learnqa.ru/ajax/api/longtime_job"

# 1
response_create_task = requests.get(url)
response_create_task_json = json.loads(response_create_task.text)
seconds = response_create_task_json['seconds']
token = response_create_task_json['token']

params = {"token": token}

# 2
response_status_check_before_task_is_done = requests.get(url, params=params)
response_json_before_task_is_done = json.loads(response_status_check_before_task_is_done.text)
if response_json_before_task_is_done['status'] == "Job is NOT ready":
    print("✔", end=' ')
    print(f"Status parameter before task is done is - \"{response_json_before_task_is_done['status']}\"")
else:
    print("✖", end=' ')
    print(f"Status parameter before task isn't done is - \"{response_json_before_task_is_done['status']}\"")

# 3
time.sleep(seconds)

# 4
response_status_check_when_task_is_done = requests.get(url, params=params)
response_status_check_when_task_is_done_json = json.loads(response_status_check_when_task_is_done.text)
if response_status_check_when_task_is_done_json['status'] != "Job is NOT ready":
    print("✔", end=' ')
    print(f"Status parameter when task is done is - \"{response_status_check_when_task_is_done_json['status']}\"")
else:
    print("✖", end=' ')
    print(f"Status parameter when task isn't done is - \"{response_status_check_when_task_is_done_json['status']}\"")

if response_status_check_when_task_is_done_json['result'] != "":
    print("✔", end=' ')
    print(f"Result parameter when task is done is - \"{response_status_check_when_task_is_done_json['result']}\"")
else:
    print("✖", end=' ')
    print(f"Result parameter when task isn't done is - \"{response_status_check_when_task_is_done_json['result']}\"")