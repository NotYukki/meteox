import requests
import matplotlib.pyplot as plt
from datetime import datetime

def get_weather(city="Chelles"):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erreur :", response.status_code)
        return None

def plot_weather(data):
    dates = []
    temps = []

    weather_days = data["weather"]
    for day in weather_days:
        date_str = day["date"]
        temps_day = [int(hour["tempC"]) for hour in day["hourly"]]
        avg_temp = sum(temps_day) / len(temps_day)
        dates.append(datetime.strptime(date_str, "%Y-%m-%d"))
        temps.append(avg_temp)

    plt.figure(figsize=(8, 5))
    plt.plot(dates, temps, marker="o", linestyle="-", color="blue")
    plt.title("Température moyenne sur les 3 prochains jours")
    plt.xlabel("Date")
    plt.ylabel("Température (°C)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    city = "Paris"
    data = get_weather(city)
    if data:
        plot_weather(data)
