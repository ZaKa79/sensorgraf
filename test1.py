import sqlite3

# connect to the database
conn = sqlite3.connect('dht11.db')
cursor = conn.cursor()

cursor.execute("SELECT datetime, temperature , humidity FROM readings")
data = cursor.fetchall()

# separate the columns into x and y lists
time = [row[0].split(' ').pop(1) for row in data]
temp = [row[1] for row in data]
hum = [row[2] for row in data]

new_time = time
print(new_time)
# close the connection
conn.close()