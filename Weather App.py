import requests

# API Keys from https://home.openweathermap.org/
API_KEY = "d8bfd7e084baba701fb45bbf40c71f0a"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    
    #Grabbing information from JSON file 
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        
    #Printing information from JSON file
        print(f"Weather in {city}")
        print(f"Conditions: {weather}")
        print(f"Temperature:{temp}")
        print(f"Humidity: {humidity}")
        

    else:
        print("City not found, please check the spelling, and try again.")

# Asks user to enter city name to find the weather in that city
city_name = input("Want to know the weather in your city? Please enter your city name! ")
weather(city_name)