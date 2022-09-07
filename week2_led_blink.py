#Example of blinking the built-in LED
#Amy Kang
#09/07/2022

#Resource: https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/creating-and-editing-code

print("let's blink")

import board
import digitalio #gives acess to pins
import time

print("it is now " + str(time.monotonic()))

led = digitalio.DigitalInOut(board.LED) #create variable that gives acess to the hardware pin
led.direction = digitalio.Direction.OUTPUT #set led pin as output so we can turn it on/off

startTime = time.monotonic() #record start time
duration = 5 #set how long to blink for (seconds)

print("start")

while (time.monotonic() - startTime) < duration:
    led.value = True
    time.sleep(0.5 / 2)
    led.value = False
    time.sleep(0.5 / 2)
    print("  runtime - %.1f" % time.monotonic())

print("all done")
