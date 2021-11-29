import serial
import sqlite3
import sys
import time

db_connection = sqlite3.connect("sensor_data.db")
db_cursor = db_connection.cursor()

sleep_time = 10

port = None

test_case = ['AA', 'C0', 'D4', '04', '3A', '0A', 'A1', '60', '1D', 'AB']
test = False

def verify_checksum(data):
    checksum = 0
    for i in range(2, 8):
        checksum += int.from_bytes(data[i], byteorder="big")

    checksum %= 256

    return checksum == int.from_bytes(data[8], byteorder="big")

# blocking
def get_data(packet):
    # if this is not the start of the packet or is an invalid packet
    if packet[0] != b'\xAA':
        print("Invalid packet header '" + packet[0].hex() + "', skipping...")
        return None
    
    if packet[1] != b'\xC0':
        print("Packet with command '" + packet[1].hex() + "' is not a query reply packet")
        return None

    if verify_checksum(packet) == False:
        print("Checksum failed for packet, skipping...")
        return None

    pm25 = ((int.from_bytes(packet[3], byteorder="big") * 256) + int.from_bytes(packet[2], byteorder="big")) / 10
    pm10 = ((int.from_bytes(packet[5], byteorder="big") * 256) + int.from_bytes(packet[4], byteorder="big")) / 10

    print("pm2.5=" + str(pm25) + ", pm10=" + str(pm10))

    return {"pm2.5": pm25, "pm10": pm10}

def get_packet():
    data = []
    for i in range(10):
        byte = port.read()
        data.append(byte)

    return data

def save_data(pm25, pm10):
    db_cursor.execute("INSERT INTO PM25 (timestamp, value) VALUES(datetime('now'), :value)", {"value": pm25})
    db_cursor.execute("INSERT INTO PM10 (timestamp, value) VALUES(datetime('now'), :value)", {"value": pm10})
    db_connection.commit()

def poll():
    while True:
        data = get_data(get_packet())

        if data != None:
            save_data(data["pm2.5"], data["pm10"])

        time.sleep(sleep_time)

def main():
    if not test:
        if len(sys.argv) != 2:
            print("Usage: " + sys.argv[0] + " device_path")
            return 1

        port = serial.Serial(sys.argv[1]) # probably /dev/ttyUSB0

        poll()
    else:
        packet = []
        for i in range(10):
            packet.append(bytes.fromhex(test_case[i]))

        print(get_data(packet))
    

if __name__ == '__main__':
    main()