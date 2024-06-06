from microbit import *
import radio

RECEIVE_GROUP = 1
TRANSMIT_GROUP = 2

radio.on()
radio.config(group=TRANSMIT_GROUP)
radio.config(power=7)

while True:
    message = radio.receive()
    if message:
        radio.config(group=RECEIVE_GROUP)
        radio.send(message)
        radio.config(group=TRANSMIT_GROUP)
        display.scroll("SENT")