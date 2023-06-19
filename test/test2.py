import serial

# Open the serial port
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Replace '/dev/ttyUSB0' with your USB port name and the baud rate



# Read data from the serial port
while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode('utf-8').rstrip()  # Read a line of data and decode it
        print(data)  # Print the received data

# Close the serial port when you're done
ser.close()
