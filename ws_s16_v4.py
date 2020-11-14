
c# Importing the GPIO library to use the GPIO pins of Raspberry pi
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)  # Using BCM numbering
host = ""
port = 1        # Raspberry Pi uses port 1 for Bluetooth Communication
###################################################
import time
from adafruit_servokit import ServoKit

#flsk
from flask import Flask, request, Response
from flask_cors import CORS


# esto lo utilizamos solo para desactivar el gpo4, para cable colores
import RPi.GPIO as GPIO
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, False)

#inicializa  8 cancles
kit = ServoKit(channels=8)


app = Flask(__name__)

############## esto es para evitar el  "No 'Access-Control-Allow-Origin'"
CORS(app, support_credentials=True)


@app.route('/slider',methods=['POST'])

def slider():
    servo = int(request.form["servo"])
    angulo = request.form["grados"]
    kit.servo[int(servo)].angle = int(angulo)
    return str(angulo)

if __name__=="__main__":
        app.run(host="192.168.1.45", port=8080)

