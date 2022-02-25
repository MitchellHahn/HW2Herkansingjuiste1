import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
#import GPIO as GPIO

#GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(21, GPIO.OUT)  #led1 output pin
GPIO.setup(26, GPIO.OUT)   #led2 output pin
GPIO.setup(19, GPIO.IN)    #button input pin

#knipper snelheiden
snelheid2= 3
snelheid1= 1

#tijden
tijd1= 0
tijd2= 0

counter= 0
gpio = [GPIO.LOW, GPIO.HIGH]
teller = 0

try:
    while True: # Run forever
     if GPIO.input(19):
      counter += 1
     else:
      counter = 0
     if counter == 1:
      GPIO.output(21, gpio[teller % 2])
      teller += 1
finally:
 GPIO.cleanup()
