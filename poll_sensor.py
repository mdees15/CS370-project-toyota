import pyserial
import sqlite3
import sys
import time

db_connection = sqlite3.connect("sensor_data.db")
db_cursor = db_connection.cursor()

sleep_time = 10

port = None

def verify_checksum(data):
    checksum = 0
    for i in range(2, 8):
        checksum += data[i]

    checksum %= 256

    return checksum == data[8]

# blocking
def get_data():
    data = []
    for i in range(10):
        byte = port.read()
        data.append(byte)

    # if this is not the start of the packet or is an invalid packet
    if data[0] != b'\xAA':
        print("Invalid packet header '{}', skipping...", data[0])
        return None
    
    if data[1] != b'\xC0':
        print("Packet with command '{}' is not a query reply packet", data[1])
        return None

    if verify_checksum == False:
        print("Checksum failed for packet, skipping...")
        return None

    pm25 = ((data[3] * 256) + data[2]) / 10
    pm10 = ((data[5] * 256) + data[4]) / 10

    return {"pm2.5": pm25, "pm10": pm10}

def save_data(pm25, pm10):
    db_cursor.execute("INSERT INTO PM25 (timestamp, value) VALUES(datetime('now'), :value)", {"value": pm25})
    db_cursor.execute("INSERT INTO PM10 (timestamp, value) VALUES(datetime('now'), :value)", {"value": pm10})
    db_connection.commit()

def poll():
    while True:
        data = get_data()

        if data != None:
            save_data(data["pm2.5"], data["pm10"])

        time.sleep(sleep_time)

def main():
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " device_path")
        return 1

    port = serial.Serial(sys.argv[1]) # probably /dev/ttyUSB0

    poll()
    

if __name__ == '__main__':
    main()