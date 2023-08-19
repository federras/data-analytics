from utils import get_weather_data
from flask import Flask, render_template, jsonify, request
import control
from database import db
from config import Config

config = Config()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI

# Inicializa la instancia de SQLAlchemy con la aplicación Flask
db.init_app(app)

# Ruta de inicio
@app.route('/', methods=['GET', 'POST'])
def index():
    return control.index()

# API para obtener datos de una ciudad, query ciudad
@app.route('/api/weather', methods=['GET'])
def get_weather():
    return control.get_weather()


# Ruta muestra datos del clima de la DB
@app.route('/mostrar_datos', methods=['GET'])
def mostrar_datos():
    return control.mostrar_datos()

if __name__ == '__main__':
    app.run(debug=True)