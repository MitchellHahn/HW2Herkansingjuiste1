# Import Raspberry Pi GPIO library
import RPi.GPIO as GPIO
import time

#knopen en poort
knop1 = 4
knop2 = 14

GPIO.setmode(GPIO.BCM)

# button 1 en 2 input
GPIO.setup(knop1, GPIO.IN)
GPIO.setup(knop2, GPIO.IN)

#motor
GPIO.setup(5, GPIO.OUT)

#pwm
pwm = GPIO.PWM(5, 50)
pwm.start(0)
hoek = 0

def SetAngle(angle):
    duty = angle / 18 + 2.5
    pwm.ChangeDutyCycle(duty)

while True:
    #Snelheid per knop
    slow = GPIO.input(knop2)
    fast = GPIO.input(knop1)
    if slow or fast:

        print("1 seconde " + str(slow))
        print(" half seconde " + str(fast))
        #heen
        while hoek < 120:
            SetAngle(hoek)
            time.sleep(0.1)
            if GPIO.input(knop2):
                time.sleep(0.1)
            hoek = hoek + 30
            print(hoek)
        #terug
        while hoek > 0:
            SetAngle(hoek)
            time.sleep(0.1)
            if GPIO.input(knop2):
                time.sleep(0.1)

            hoek = hoek - 30
            print(hoek)