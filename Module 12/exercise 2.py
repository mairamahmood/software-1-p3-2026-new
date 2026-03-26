import requests

city = input("Enter city name: ")
api_key = "9d37653ca5d59aff68f724edd5178fec"

url_1= f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"

response = requests.get(url_1)

if response.status_code == 200:
    data = response.json()
    for item in data:
      name  = item["name"]
      latitude  = item["lat"]
      longitude  = item["lon"]
      country_name = item["country"]

      print(name,country_name)
else:
    print("Error fetching weather data.")

url_2= f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=metric&appid={api_key}"
response = requests.get(url_2)

if response.status_code == 200:
    data = response.json()
    print(data ["weather"][0]["description"])
    print(f"{data['main']['temp']} C")
else:
    print("Error fetching weather data.")


