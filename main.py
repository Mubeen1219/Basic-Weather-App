import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "41038a74474e4f74a026eea16f1fcffc"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Fetch weather function
def get_weather():
    city = city_entry.get().strip()
    
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data.get("cod") != 200:
            messagebox.showerror("Error", f"City '{city}' not found.")
            return

        city_name = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description'].title()

        result = f"City: {city_name} ({country})\nTemperature: {temp} °C\nHumidity: {humidity}%\nConditions: {description}"
        result_label.config(text=result)

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# GUI setup
window = tk.Tk()
window.title("Weather App")
window.geometry("400x300")
window.config(bg="#f0f0f0")

tk.Label(window, text="Enter City Name:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
city_entry = tk.Entry(window, font=("Arial", 12), width=30)
city_entry.pack(pady=5)

tk.Button(window, text="Get Weather", command=get_weather, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12), bg="#f0f0f0", justify="left")
result_label.pack(pady=10)

tk.Button(window, text="Exit", command=window.quit, font=("Arial", 10), bg="red", fg="white").pack(pady=10)

window.mainloop()
