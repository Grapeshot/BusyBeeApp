import json
import requests

city = 'Atlanta' # default to Atlanta
WEATHER_API_KEY = 'b1c948b41c7ea950b504b755d258629d'

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

print(data)