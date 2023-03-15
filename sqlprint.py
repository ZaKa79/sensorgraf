import sqlite3

conn = sqlite3.connect('dht11.db')

try: 
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM readings")
    rows = cursor.fetchall()
    print(f'Row-count :{ len(rows) }')
    for row in rows:
        #print(f'Data = {row[1]} temperature={row[2]} humidity={row[3]}')
        temp = row[2]
        print(temp)
        humi = row[3]
        #print(humi)
# Close the cursor and connection
except sqlite3.Error as e:
    print(f'Error calling SQL: "{e}"')
finally:
    cursor.close()
    conn.close()
