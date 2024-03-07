from flask import Flask, render_template
from sensor_reader import get_sensor_data

app = Flask(__name__)

@app.route('/')
def index():
    sensor_data = get_sensor_data()
    return render_template('index.html', data = sensor_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080, ssl_context=('server.crt', 'server.key'))
