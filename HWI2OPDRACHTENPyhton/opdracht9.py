import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
import time

# import GPIO as GPIO

# GPIO.setwarnings(False) # Ignore warning for now

#vier led input van Arduino naar raspberry
GPIO.setmode(GPIO.BCM)  # Use physical pin numbering
GPIO.setup(21, GPIO.IN)
GPIO.setup(11, GPIO.IN)
GPIO.setup(9, GPIO.IN)
GPIO.setup(13, GPIO.IN)

#vier led output van raspberry naar LED's en breadboard
GPIO.setup(7, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)

gpio = [GPIO.LOW, GPIO.HIGH]

try:
    while True:
        # input van Arduino naar raspberry koppelen met output van raspberry naar LED's en breadboard
        GPIO.output(7, gpio[GPIO.input(21)])
        GPIO.output(14, gpio[GPIO.input(11)])
        GPIO.output(12, gpio[GPIO.input(9)])
        GPIO.output(8, gpio[GPIO.input(13)])


finally:
    GPIO.cleanup()