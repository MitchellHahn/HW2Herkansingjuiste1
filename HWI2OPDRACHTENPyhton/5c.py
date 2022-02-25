#buttonInput.py
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#sleepTime = .1

#GPIO Pin of the component
lightPin1 = 8
lightPin2 = 5

button1 = 14

#MILLIS STATE
mil1 = time.time()

GPIO.setup(button1, GPIO.IN)
#GPIO.setup(button2, GPIO.IN)

GPIO.setup(lightPin1, GPIO.OUT)
GPIO.setup(lightPin2, GPIO.OUT)


try:
    while True:
        if GPIO.input(button1):

            GPIO.output(lightPin1, GPIO.HIGH)
            GPIO.output(lightPin2, GPIO.LOW)

            if mil1 +1 < time.time():
                GPIO.output(lightPin1, GPIO.LOW)
                GPIO.output(lightPin2, GPIO.HIGH)

            if mil1 +2 < time.time():
                mil1 = time.time()
        else:
            GPIO.output(lightPin1, GPIO.HIGH)
            GPIO.output(lightPin2, GPIO.LOW)
            if mil1 + 1.3 < time.time():
                GPIO.output(lightPin1, GPIO.LOW)
                GPIO.output(lightPin2, GPIO.HIGH)
            if mil1 + 2 < time.time():
                mil1 = time.time()

        time.sleep(0.1)
finally:
          GPIO.cleanup()