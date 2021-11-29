from flask import Flask, render_template
import sqlite3
import json

app = Flask(__name__)

db_connection = sqlite3.connect("sensor_data.db", detect_types=sqlite3.PARSE_DECLTYPES)
db_cursor = db_connection.cursor()

num_data_limit = 100

@app.route("/")
def get_page():
    return render_template("index.html")

@app.route("/get_data")
def get_data():
    data = {"pm25": [], "pm10": []}
    for row in db_cursor.execute("SELECT * FROM PM25 ORDER BY timestamp ASC LIMIT :limit", {"limit": num_data_limit}):
        data["pm25"].append({"timestamp": row[0].timestamp(), "value": row[1]})

    for row in db_cursor.execute("SELECT * FROM PM10 ORDER BY timestamp ASC LIMIT :limit", {"limit": num_data_limit}):
        data["pm10"].append({"timestamp": row[0].timestamp(), "value": row[1]})

    return json.dumps(data)

def main():
    app.run(port=5000)

if __name__ == '__main__':
    main()