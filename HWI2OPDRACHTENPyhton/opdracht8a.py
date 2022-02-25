import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

#import GPIO as GPIO

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

#len 1 en 2 pins
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)




while True: # Run forever


 #aan led1
#uit led2
 GPIO.output(21, GPIO.HIGH)
 GPIO.output(26, GPIO.LOW)
 sleep(1) # Sleep for 1 second

 #uit led1
#uit led2
 GPIO.output(21, GPIO.LOW)
 GPIO.output(26, GPIO.HIGH)
 sleep(1) # Sleep for 1 second


