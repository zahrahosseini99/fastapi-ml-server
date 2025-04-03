import requests

url = "http://127.0.0.1:8000/predict"
payload = {"data": [5.1, 3.5, 1.4, 0.2]}
response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())
