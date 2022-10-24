"""Example for Pico. Blinks the built-in LED."""
import time
import board
import digitalio
 
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

relay = digitalio.DigitalInOut(board.GP16)
relay.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

unlock_duration = 5
elapsed_time = 0

while True:
    while elapsed_time < unlock_duration:
        if button.value:
            elapsed_time += 0.001
            time.sleep(0.001)
            print(elapsed_time)
        else:
            elapsed_time = 0

    led.value = True
    relay.value = True