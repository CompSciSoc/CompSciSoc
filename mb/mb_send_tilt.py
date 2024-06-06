from microbit import accelerometer as gyro

while True:
    print(gyro.get_x(), gyro.get_y(), gyro.get_z())
