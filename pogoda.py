import os
import requests

def pobierz_pogode(miasto):
    klucz_api = os.getenv('OPENWEATHERMAP_API_KEY')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={miasto}&appid={klucz_api}&units=metric&lang=pl"
    response = requests.get(url)
    if response.status_code == 200:
        dane = response.json()
        temperatura = dane['main']['temp']
        opis = dane['weather'][0]['description']
        return f"Pogoda w {miasto}: {temperatura:.1f}°C, {opis}"
    else:
        return f"Wystąpił błąd podczas pobierania danych pogodowych: {response.status_code}"

miasto = input("Podaj nazwę miasta: ")
print(pobierz_pogode(miasto))
