import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
#import GPIO as GPIO

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

snelheid2= 3
snelheid1= 1
tijd1= 0
tijd2= 0

try:
    while True: # Run forever

        #leds aan doen
     if(tijd1 + snelheid1 < time.time()):
      GPIO.output(21, GPIO.HIGH)
     if(tijd2 + snelheid2 < time.time()):
      GPIO.output(26, GPIO.HIGH)

         #uit na de tijd en resetten
     if (tijd1 + snelheid1*2 < time.time()):
      tijd1 = time.time()
      GPIO.output(21, GPIO.LOW)
     if (tijd2 + snelheid2*2 < time.time()):
      tijd2 = time.time()
      GPIO.output(26, GPIO.LOW)

finally:
 GPIO.cleanup()
