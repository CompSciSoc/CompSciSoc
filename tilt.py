import serial

ser = serial.Serial('COM3', 115200)

def getTiltData():
    '''Reads the serial data from the MicroBit and returns the tilt data as a tuple of integers.'''
    noData = True
    while noData:
        for i in range(2):
            line = ser.readline().decode('utf-8').strip()
        if line:
            splitLine = line.split('_')
            mgx = int(splitLine[0])
            mgy = int(splitLine[1])
        noData = False
    return mgx, mgy