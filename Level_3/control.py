from flask import render_template, jsonify, request
from utils import get_weather_data
from sqlalchemy import text, create_engine
from database import db, conect_DB

def index():
    weather_data = None

    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)
    return render_template('index.html', weather_data=weather_data)

def get_weather():
    city = request.args.get('city')

    if not city:
        return jsonify({'error': 'Debe proporcionar el nombre de una ciudad.'}), 400

    weather_data = get_weather_data(city)

    if not weather_data:
        return jsonify({'error': 'No se pudo obtener los datos climáticos para la ciudad proporcionada.'}), 404

    return jsonify(weather_data), 200


def mostrar_datos():
    conect_DB()
    data = obtener_datos_clima()
    return render_template('mostrar_datos.html', data=data)


def obtener_datos_clima():
    """Obtener todos los datos del clima"""
    query = text("SELECT ciudad, dia, temperatura, humedad, descripcion FROM weather_data")
    result = db.session.execute(query)
    rows = result.fetchall()
    print(rows)
    if not rows:
        return jsonify({'mensaje': 'No se encontraron datos del clima'}), 404

    data = [{
        'ciudad': row.ciudad,
        'dia': str(row.dia),
        'temperatura': row.temperatura,
        'humedad': row.humedad,
        'descripcion': row.descripcion,
    } for row in rows]

    return data