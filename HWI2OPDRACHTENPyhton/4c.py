#buttonInput.py
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

sleepTime = .1

#GPIO Pin of the component
lightPin1 = 8
lightPin2 = 5

button = 14

GPIO.setup(lightPin1, GPIO.OUT)
GPIO.setup(button, GPIO.IN)
GPIO.output(lightPin1, False)

GPIO.setup(lightPin2, GPIO.OUT)
##GPIO.setup(button, GPIO.IN)
GPIO.output(lightPin2, True)



try:
    while True:
        buttonState = GPIO.input(button)
#voert simulatie uit
        if buttonState == GPIO.HIGH:

            GPIO.output(5, GPIO.LOW)  # Turn off

            GPIO.output(8, GPIO.HIGH)  # Turn on
            sleep(1)  # Sleep for 1 second
            GPIO.output(8, GPIO.LOW)  # Turn off
            sleep(1)  # Sleep for 1 second

            sleep(sleepTime)

        else:
            #led 1 aan led 2 uit als de knop wordt los gelaten
            GPIO.output(5, GPIO.HIGH)
            GPIO.output(8, GPIO.LOW)

finally:
          GPIO.cleanup()

