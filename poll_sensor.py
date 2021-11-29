from os import error
import pyserial
import sqlite3
import sys

db_connection = sqlite3.connect("sensor_data.db")
db_cursor = db_connection.cursor()

port = None

# this is blocking
def get_data():
    data = []
    for i in range(10):
        byte = port.read()
        data.append(byte)

    # if this is not the start of the packet or is an invalid packet
    if data[0] != b'AA':
        print("Invalid packet header '{}', skipping...", data[0])
        return
    
    if data[1] != b'C0':
        print("Packet with command '{}' is not a query reply packet", data[1])
        return

    


def main():
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " device_path")
        return 1

    port = serial.Serial(sys.argv[1]) # probably /dev/ttyUSB0

    return 0
    

if __name__ == '__main__':
    main()