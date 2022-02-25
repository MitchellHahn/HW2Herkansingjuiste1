import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
#import GPIO as GPIO

#GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

#output van de raspberry naar de led's en breadboard
GPIO.setup(21, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

#input van arduino naar raspberry
GPIO.setup(9, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(11, GPIO.IN)

gpio = [GPIO.LOW, GPIO.HIGH]


try:
  while True:
    # input van arduino naar raspberry en output van de raspberry naar de led's en breadboard kopelen
    #led1
    GPIO.output(26, gpio[GPIO.input(9)])
    #knpop
    GPIO.output(21, gpio[GPIO.input(13)])
    #led2
    GPIO.output(19, gpio[GPIO.input(11)])

finally:
 GPIO.cleanup()
