import base64
from io import BytesIO
from flask import Flask
from flask import render_template
from matplotlib.figure import Figure
import sqlite3

# connect to the database
conn = sqlite3.connect('dht11.db')
cursor = conn.cursor()

cursor.execute("SELECT datetime, temperature , humidity FROM readings")
data = cursor.fetchall()

# separate the columns into x and y lists (pop removes date)
time = [row[0].split(' ').pop(1) for row in data]
temp = [row[1] for row in data]
hum = [row[2] for row in data]

# close the connection
conn.close()

app = Flask(__name__)
@app.route("/")

def home():
    return render_template ("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
def hello():
    fig = Figure()
    ax = fig.subplots()
    y = [temp[-4], temp[-3], temp[-2], temp[-1]]
    x = [time[0], time[1], time[2], time[3]]
    ax.set_facecolor("#000") # inner plot background color HTML black
    fig.patch.set_facecolor('#000') # outer plot background color HTML black
    ax.plot(x, y, linestyle = 'dashed', c = '#11f', linewidth = '1.5', marker = 'o', mec = 'hotpink', ms = 10, mfc = 'hotpink' )
    ax.set_xlabel('Time')
    ax.set_ylabel('Temperature')
    ax.xaxis.label.set_color('hotpink') #setting up X-axis label color to hotpink
    ax.yaxis.label.set_color('hotpink') #setting up Y-axis label color to hotpink
    ax.tick_params(axis='x', colors='white') #setting up X-axis tick color to white
    ax.tick_params(axis='y', colors='white') #setting up Y-axis tick color to white
    ax.spines['left'].set_color('blue') # setting up Y-axis tick color to blue
    ax.spines['top'].set_color('blue') #setting up above X-axis tick color to blue
    ax.spines['bottom'].set_color('blue') #setting up above X-axis tick color to blue
    ax.spines['right'].set_color('blue') #setting up above X-axis tick color to blue
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"
if __name__ == "__main__":
    app.run()
