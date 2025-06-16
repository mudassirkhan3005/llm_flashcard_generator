import requests

url = "http://127.0.0.1:8000/generate"
data = {
    "text": "Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods with the help of chlorophyll.",
    "subject": "Biology"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.json())
