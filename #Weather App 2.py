#Weather App 2
import requests

response = requests.get("https://ipinfo.io/json")

data = response.json()

print(data)