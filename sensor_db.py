import sqlite3
from datetime import datetime 
import RPi.GPIO as GPIO
import dht11
from time import sleep

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read sensor data using pin 14
instance = dht11.DHT11(pin = 14)
result = instance.read()


def insertDHTDATA():
    try:
        dt = datetime.now().strftime('%d-%m-%Y %H.%M.%S') #time ande date
        conn = sqlite3.connect('dht11.db')
        query ='INSERT INTO DHT11TABLE (DATETIME, TEMPERATURE, HUMIDITY)VALUES(?,?,?)'
        
        if result.is_valid(): #from sencor
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)

            # Create a database/table
            conn = sqlite3.connect('dht11.db') #connect to Database
            c = conn.cursor() #make a cursor
            c.execute("CREATE TABLE IF NOT EXISTS readings (id integer PRIMARY KEY AUTOINCREMENT, datetime timestamp, temperature float, humidity float)") #creates the database 

            query = "INSERT INTO readings (DateTime,Temperature,Humidity) VALUES (?,?,?)" #setup for injection
            values = (dt,result.temperature, result.humidity) # the values
            c.execute (query, values)
            conn.commit() #send values
        else: #from sensor
            print("Error: %d" % result.error_code)
    except sqlite3.Error as e:
        conn.rollback()
        print(f'Could not insert ! {e}')
    finally:
        conn.close()

#print(result.temperature)
while True: 
    insertDHTDATA()
    sleep(10)