"""Example for Pico. Blinks the built-in LED."""
import time
import board
import digitalio
 
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

relay = digitalio.DigitalInOut(board.GP16)
relay.direction = digitalio.Direction.OUTPUT

 
while True:
    led.value = True
    relay.value = True
    time.sleep(0.5)
    led.value = False
    relay.value = False
    time.sleep(0.5)