import Adafruit_DHT
import RPi.GPIO as GPIO
import time

TEMP_SENSOR = Adafruit_DHT.DHT11
TEMP_SENSOR_PIN = 4
LIGHT_SENSOR_PIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT_SENSOR_PIN, GPIO.IN)

def get_sensor_data():
    humidity, temperature = Adafruit_DHT.read_retry(TEMP_SENSOR,TEMP_SENSOR_PIN)
    light = GPIO.input(LIGHT_SENSOR_PIN)
    if humidity is not None and temperature is not None and light is not None:
        if light == 0:
            light = 'Bright'
        elif light == 1:
            light = 'Dark'
        return {'temperature':temperature, 'airhumidity':humidity, 'light': light}
    else:
        return {'temperature': 'N/A', 'airhumidity': 'N/A'}
    
if __name__ == "__main__":
    while True:
        data = get_sensor_data()
        print(f"Temperature: {data['temperature']} C, Humidity: {data['airhumidity']} %, Light: {data['light']}")
        time.sleep(2)