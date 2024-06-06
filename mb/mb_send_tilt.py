from microbit import accelerometer as gyro

while True:
    x, y, z = gyro.get_x(), gyro.get_y(), gyro.get_z()
    print(str(x) + ' ' + str(y) + ' ' + str(z))
