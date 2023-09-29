import requests

payload = {"X": [[101, 3]]}
url = "http://localhost:5000/predict"
response = requests.post(url, json=payload)
print(response.json())
