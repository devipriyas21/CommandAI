import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(state, district):

    places = [
        district,
        f"{district}, {state}",
        f"{district}, India",
        state
    ]

    for place in places:

        try:

            url = (
                f"https://api.openweathermap.org/data/2.5/weather"
                f"?q={place}&appid={API_KEY}&units=metric"
            )

            response = requests.get(url)

            if response.status_code == 200:

                data = response.json()

                return {
                    "temperature": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                    "wind": data["wind"]["speed"],
                    "condition": data["weather"][0]["description"].title()
                }

        except:
            continue

    return None