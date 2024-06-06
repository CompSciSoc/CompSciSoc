
import serial
import keyboard

ser = serial.Serial('COM3', 115200)

lastGesture = None
while True:
    _    = ser.readline().decode('utf-8').strip() 
    line = ser.readline().decode('utf-8').strip()
    if lastGesture != line:
        lastGesture = line
        if line == 'up':
            keyboard.press('w')
            keyboard.release('w')
        elif line == 'down':
            keyboard.press('s')
            keyboard.release('s')
        elif line == 'left':
            keyboard.press('a')
            keyboard.release('a')
        elif line == 'right':
            keyboard.press('d')
            keyboard.release('d')
        elif line == 'shake':
            keyboard.press('space')
            keyboard.release('space')