import config
import requests

def get_coordenadas(city):
    URL=f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={config.OPENWEATHER_API_KEY}"
    response = requests.get(URL)
    # print(response.json())
    if response.json() or response.status_code != 200:
        data = response.json()
        lat = data[0]["lat"]
        lon = data[0]["lon"]
        coord = f'lat={lat}&lon={lon}'
        return coord
    else:
        print(f"Error {city} no esta en la base de datos")
        return None

def get_nombre_ciudad_by_coord(coord):
    URL=f"http://api.openweathermap.org/geo/1.0/reverse?{coord}&limit=5&appid={config.OPENWEATHER_API_KEY}"
    response = requests.get(URL)
    if response.json() or response.status_code != 200:
        data = response.json()
        nombre = data[0]["name"]
        return nombre
    else:
        print(f"Error {coord} no esta en la base de datos")
        return None
