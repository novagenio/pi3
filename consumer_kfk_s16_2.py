import json
# Importing the GPIO library to use the GPIO pins of Raspberry pi
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)  # Using BCM numbering
host = ""
port = 1        # Raspberry Pi uses port 1 for Bluetooth Communication
###################################################
import time
from adafruit_servokit import ServoKit

# kafka
from kafka import KafkaConsumer
consumer = KafkaConsumer('topic-basic-test', bootstrap_servers=['techhublabs.com:9092'],group_id='topic-basic-test')


# esto lo utilizamos solo para desactivar el gpo4, para cable colores
import RPi.GPIO as GPIO
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, False)

#inicializa  8 cancles
kit = ServoKit(channels=8)

for msg in consumer:
        data=json.loads(msg.value)
        print ("Valores inicio Servo: " +  str(data['Servo']) + " Grados: " +  str(data['Grados']))
        servo = data['Servo']
        grados = data['Grados']
        kit.servo[int(servo)].angle = int(grados)


