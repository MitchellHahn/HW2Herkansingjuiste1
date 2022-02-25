#buttonInput.py
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#sleepTime = .1

#GPIO Pin of the component
lightPin1 = 8
lightPin2 = 5

button1 = 14
button2 = 4

mil1 = time.time()

GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)

GPIO.setup(lightPin1, GPIO.OUT)
GPIO.output(lightPin1, False)

GPIO.setup(lightPin2, GPIO.OUT)
GPIO.output(lightPin2, False)




try:
    while True:
        buttonState1 = GPIO.input(button1)
        buttonState2 = GPIO.input(button2)

        if buttonState1 == GPIO.HIGH:

            #led1 uit
            GPIO.output(8, GPIO.LOW)  # Turn off
            #led1 aan
            if mil1 +0.7 < time.time():
                GPIO.output(8, GPIO.HIGH)  # Turn on
            if mil1 +0.7 < time.time():
                mil1= time.time()

        if buttonState2 == GPIO.HIGH:

            #led2 uit
            GPIO.output(5, GPIO.LOW)  # Turn off
            # led2 aan
            if mil1 +1 < time.time():
                GPIO.output(5, GPIO.HIGH)  # Turn on
            if mil1 +1 < time.time():
                mil1= time.time()

finally:
          GPIO.cleanup()

