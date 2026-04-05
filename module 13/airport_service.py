from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="testuser",
        password="123",
        database="flight_game"
    )



@app.route("/airport/<string:icao_code>", methods=["GET"])
def get_airport(icao_code):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name, municipality FROM airport WHERE ident = %s",
        (icao_code.upper(),)
    )
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        name, location = result
        return jsonify({
            "ICAO": icao_code.upper(),
            "Name": name,
            "Location": location
        })
    else:
        return jsonify({
            "ICAO": icao_code.upper(),
            "error": "Airport not found"
        }), 404



if __name__ == "__main__":
    app.run(debug=True, port=5002)