# Función para obtener datos climáticos de OpenWeatherMap
import requests
import config

def get_weather_data(city):

    #Cargamos variable de entorno
    api_key = config.OPENWEATHER_API_KEY
    if not api_key:
        raise ValueError("No se encontró la clave de API de OpenWeatherMap. "
                         "Asegúrate de configurar la variable de entorno 'OPENWEATHERMAP_API_KEY'.")
    

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        weather = {
            'city': data['name'],
            'description': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
        }
        return weather

    return None