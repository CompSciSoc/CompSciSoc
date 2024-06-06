import serial

ser = serial.Serial('COM3', 115200)

def getRawTiltData():
    '''Reads the serial data from the MicroBit and returns the tilt data as a tuple of integers.'''
    noData = True
    while noData:
        line = ser.readline().decode('utf-8').strip()
        try:
            splitLine = line.split()
            mgx = int(splitLine[0])
            mgy = int(splitLine[1])
        # if the line is not in the expected format, ignore it and try again
        except ValueError:
            continue
        noData = False
    return mgx, mgy

def getTiltData():
    '''Reads the serial data from the MicroBit and returns the tilt data scaled to between 0-10 as a tuple of integers.'''
    noData = True
    while noData:
        line = ser.readline().decode('utf-8').strip()
        try:
            splitLine = line.split()
            mgx = int(splitLine[0])
            mgy = int(splitLine[1])
        # if the line is not in the expected format, ignore it and try again
        except ValueError:
            continue
        noData = False
    mgx = round(mgx/100, 2)
    mgy = round(mgy/100, 2)
    return mgx, mgy