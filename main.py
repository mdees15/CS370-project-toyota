from flask import Flask, render_template
import sqlite3
import json

app = Flask(__name__)

num_data_limit = 100

@app.route("/")
def get_page():
    return render_template("index.html")

@app.route("/get_data")
def get_data():
    db_connection = sqlite3.connect("sensor_data.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    db_cursor = db_connection.cursor()

    data = {"pm25": [], "pm10": []}
    for row in db_cursor.execute('SELECT timestamp AS "timestamp [timestamp]", value AS "value [real]" FROM PM25 ORDER BY timestamp DESC LIMIT :limit', {"limit": num_data_limit}):
        data["pm25"].append({"timestamp": row[0].timestamp() * 1000, "value": row[1]})

    for row in db_cursor.execute('SELECT timestamp AS "timestamp [timestamp]", value AS "value [real]" FROM PM10 ORDER BY timestamp DESC LIMIT :limit', {"limit": num_data_limit}):
        data["pm10"].append({"timestamp": row[0].timestamp() * 1000, "value": row[1]})

    data["pm25"].reverse()
    data["pm10"].reverse()

    return json.dumps(data)

def main():
    app.run(host="0.0.0.0", port=5000)

if __name__ == '__main__':
    main()