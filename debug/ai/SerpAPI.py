import requests

API_KEY = "your_serpapi_key"
params = {
    "engine": "google_scholar",
    "q": "machine learning",
    "api_key": API_KEY
}

response = requests.get("https://serpapi.com/search", params=params)
data = response.json()

print(data)