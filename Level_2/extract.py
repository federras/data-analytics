import pandas as pd
from helpers import get_weather_data_city_list, get_weather_data_coord_list, concatenar_diccionarios, construir_nombre_archivo_csv

cityList = ["London", "New York", "Cordoba", "Taipei", "Buenos Aires", "Mexico DF", "Dublin", "Tilfis", "Bogota", "Tokio"]
coordList = ["lat=31&lon=64", "lat=40&lon=-73", "lat=-31&lon=-64", "lat=25&lon=64", "lat=-34&lon=-58", "lat=19&lon=-99", "lat=53&lon=6", "lat=41&lon=44", "lat=4&lon=74", "lat=35&lon=139"]

#Extraemos todos los datos de openWeather
ciudades = get_weather_data_city_list(cityList)
coordenadas = get_weather_data_coord_list(coordList)
total = concatenar_diccionarios(ciudades, coordenadas)

# Guardar el DataFrame en un archivo CSV
df = pd.DataFrame(total)
ruta_archivo_csv = construir_nombre_archivo_csv()
df.to_csv(ruta_archivo_csv, index=False)