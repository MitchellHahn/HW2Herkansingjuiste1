#buttonInput.py
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

sleepTime = .1

#GPIO Pin of the component
lightPin = 8
button = 14

GPIO.setup(lightPin, GPIO.OUT)
GPIO.setup(button, GPIO.IN)
GPIO.output(lightPin, False)

try:
    while True:
        GPIO.output(lightPin, GPIO.input(button))
        sleep(sleepTime)
finally:
    GPIO.output(lightPin, False)
    GPIO.cleanup()