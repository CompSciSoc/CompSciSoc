from microbit import *
import radio

MY_NAME = 'no1'

RECEIVE_GROUP = 1
TRANSMIT_GROUP = 2

radio.on()
radio.config(group=RECEIVE_GROUP)
radio.config(power=7)

while True:
    if button_a.was_pressed():
        radio.config(group=TRANSMIT_GROUP)
        radio.send(MY_NAME + '_DAP')
        radio.config(group=RECEIVE_GROUP)
    message = radio.receive()
    if message:
        message = message.split('_')
        if message[0] != MY_NAME:
            if message[1] == 'DAP':
                display.scroll('DAP')