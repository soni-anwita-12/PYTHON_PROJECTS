import json
import requests

API_KEY = "YOUR API_KEY"

def get_weather(city):

    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            print("\nWeather Information")
            print("City:", data["location"]["name"])
            print("Country:", data["location"]["country"])
            print("Temperature:", data["current"]["temp_c"], "°C")
            print("Condition:", data["current"]["condition"]["text"])
            print("Humidity:", data["current"]["humidity"], "%")
            print("Wind Speed:", data["current"]["wind_kph"], "km/h")

        else:
            print("Error:", data.get("error", {}).get("message", "Something went wrong"))

    except requests.exceptions.RequestException as e:
        print("Connection Error:", e)


city = input("Enter city name: ")
get_weather(city)