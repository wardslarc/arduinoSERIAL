# Data Collection to SQL Database via Serial Connection

## Overview

This Python script is designed for data collection from a serial port and subsequent insertion into a MySQL database, emphasizing a connection method without relying on Wi-Fi boards or wireless communication. The code uses the `serial` library to read data from a connected device, such as an Arduino, and the `mysql.connector` library to interact with a MySQL database for data storage.

## Requirements

Before running this script, ensure you have the following prerequisites installed:

- Python 3.x
- `serial` library (can be installed using `pip install pyserial`)
- `mysql.connector` library (can be installed using `pip install mysql-connector-python`)

## Usage

1. **Hardware Connection**: Connect your device (e.g., Arduino) to the specified serial port (e.g., COM3) and configure it to send data.

2. **Database Configuration**: Set up a MySQL database and provide the database credentials in the script. Replace the following placeholders with your own values:

   - `user`: Your MySQL username.
   - `password`: Your MySQL password.
   - `host`: The MySQL server's address (e.g., localhost).
   - `database`: The name of the database where you want to store the data.

3. **Running the Script**: Run the script by executing the Python file. It will continuously read data from the serial port, process it, and insert it into the specified database.

4. **Data Insertion**: The script converts the received data into float values, which are then inserted into the database table named `sensor_data`. The data should be in the format expected by the code.

## Customization

You can customize the script according to your specific requirements:

- **Serial Port Configuration**: Adjust the serial port settings (e.g., port name and baud rate) in the `ser = serial.Serial('COM3', 9600)` line to match your device configuration.

- **Database Schema**: Modify the database table and schema as needed. Ensure that the table structure in your database matches the data format that the script is trying to insert.

## Error Handling

The script includes error handling for common exceptions, such as ValueError (when converting values to float), mysql.connector.Error (for database-related errors), and serial.SerialException (for serial port communication issues). Error messages will be displayed in the console.


