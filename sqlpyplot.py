import sqlite3
import matplotlib.pyplot as plt

# connect to the database
conn = sqlite3.connect('dht11.db')
cursor = conn.cursor()

cursor.execute("SELECT datetime, temperature FROM readings")
data = cursor.fetchall()

# separate the columns into x and y lists
x = [row[0] for row in data]
y = [row[1] for row in data]

# plot the data as a scatter plot
plt.scatter(x, y)

# add labels and title
plt.xlabel('Tid')
plt.ylabel('Temperatur')
plt.title('Temperatur Graf')

# display the plot
plt.show()

# close the connection
conn.close()
