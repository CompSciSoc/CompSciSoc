from microbit import accelerometer

while True:
    gesture = accelerometer.current_gesture()
    print(gesture)