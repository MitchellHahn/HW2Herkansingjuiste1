import time
from RPi import GPIO

GPIO.setmode(GPIO.BCM)

##pin motor
gpioPins = [2, 3, 4, 17]

for p in gpioPins:
    GPIO.setup(p, GPIO.OUT)

##knopen input
GPIO.setup(9, GPIO.IN)
GPIO.setup(10, GPIO.IN)

##setting = 0

##snelheidtijd in 360 graden
langzaam = (5 - 0.0) / (512 * 8)
snel = (12 - 0.0) / (512 * 8)
##tijd state voor snelheid
timer = 0

try:
    while True:

        ##knop1
        ##links en langzaam
        while GPIO.input(9):
            for p in range(0, 4):
                for b in gpioPins:
                    GPIO.output(b, GPIO.LOW)
                GPIO.output(gpioPins[p], GPIO.HIGH)
                timer = time.perf_counter()
                while timer + langzaam > time.perf_counter():
                    pass
                GPIO.output(gpioPins[(p + 1) % 4], GPIO.HIGH)
                timer = time.perf_counter()
                while timer + langzaam > time.perf_counter():
                    pass

                ##knop 2
                #rechts en snel
        while GPIO.input(10):
            for p in range(3, -1, -1):
                for b in gpioPins:
                    GPIO.output(b, GPIO.LOW)
                GPIO.output(gpioPins[p], GPIO.HIGH)
                timer = time.perf_counter()
                while timer + snel > time.perf_counter():
                    pass
                GPIO.output(gpioPins[(p - 1) % 4], GPIO.HIGH)
                timer = time.perf_counter()
                while timer + snel > time.perf_counter():
                    pass
        for b in gpioPins:
            GPIO.output(b, GPIO.LOW)
finally:
    GPIO.cleanup()