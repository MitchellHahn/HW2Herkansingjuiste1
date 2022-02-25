import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

#import GPIO as GPIO

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

while True: # Run forever
 #aan
 GPIO.output(8, GPIO.HIGH)
 sleep(1) # Sleep for 1 second
 #uit
 GPIO.output(8, GPIO.LOW)
 sleep(1) # Sleep for 1 second