import serial
import mysql.connector
from datetime import datetime

# Open a serial connection to the Arduino
ser = serial.Serial('COM3', 9600)

# Connect to the MySQL database
cnx = mysql.connector.connect(user='escalo253', password='cawlsdale', host='localhost', database='user_db')

while True:
    try:
        # Read a line of data from the serial port
        data = ser.readline().decode().rstrip()

        # Split the data into separate values
        values = data.split(' ')

        # Convert each value to a float and store in a list
        float_values = []
        for value in values:
            try:
                float_value = float(value)
                float_values.append(float_value)
            except ValueError:
                print(f"Could not convert value {value} to float")

        # Print the converted values
        print(float_values)

        # Insert the data into the database
        cursor = cnx.cursor()
        query = "INSERT INTO sensor_data (soil_moisture, accelerometer, vegetation, rain_drop, landslide_rating) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, tuple(float_values))
        cnx.commit()
        cursor.close()

    except ValueError as err:
        print(f"Error: {err}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    except serial.SerialException as err:
        print(f"Error: {err}")
