from flask import Flask, render_template, send_from_directory, jsonify
from flask_cors import CORS
from sensor_reader import get_sensor_data
import os


# app = Flask(__name__)
app = Flask(__name__, static_folder='build')
CORS(app)  # Enable CORS for all routes

# @app.route('/')
# def index():
#     sensor_data = get_sensor_data()
#     return render_template('index.html', data = sensor_data)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/get_plant_data')
def plant_data():
    print("update button clicked, fetching sensor data")
    sensor_data = get_sensor_data()  # Assuming this returns a dictionary
    return jsonify(temperature = sensor_data['temperature']), jsonify(airhumidity = sensor_data['airhumidity'] ) # Convert the Python dictionary to JSON

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080, ssl_context=('server.crt', 'server.key'))
