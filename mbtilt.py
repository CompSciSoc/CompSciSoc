from microbit import accelerometer

while True:
    x, y, z = accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()
    print(str(x) + '_' + str(y) + '_' + str(z))
