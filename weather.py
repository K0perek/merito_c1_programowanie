import requests
import os

def pobierz_pogode(miasto, klucz_api):
    """
    Funkcja pobiera aktualną pogodę dla podanego miasta za pomocą API OpenWeatherMap.

    Args:
        miasto (str): Nazwa miasta, dla którego ma być pobrana pogoda.
        klucz_api (str): Klucz API do autoryzacji w serwisie OpenWeatherMap.

    Returns:
        str: Tekst zawierający informacje o pogodzie lub komunikat o błędzie.
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={miasto}&appid={klucz_api}&units=metric&lang=pl"
    response = requests.get(url)
    if response.status_code == 200:
        dane = response.json()
        temperatura = dane['main']['temp']
        opis = dane['weather'][0]['description']
        return f"Pogoda w {miasto}: {temperatura:.1f}°C, {opis}"
    else:
        return f"Wystąpił błąd podczas pobierania danych pogodowych: {response.status_code}"

def get_api_key():
    """
    Funkcja pobiera klucz API ze zmiennej środowiskowej OPENWEATHERMAP_API_KEY.
    """
    return os.environ.get('OPENWEATHERMAP_API_KEY')

# Pobranie klucza API ze zmiennej środowiskowej
klucz_api = get_api_key()

if klucz_api:
    miasto = input("Podaj nazwę miasta: ")
    print(pobierz_pogode(miasto, klucz_api))
else:
    print("Brak klucza API. Ustaw zmienną środowiskową OPENWEATHERMAP_API_KEY.")
