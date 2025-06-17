from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route("/data")
def data():
    # Replace with your MySQL info
    try:
        db = mysql.connector.connect(
            host="mysql-service",
            user="root",
            password="rootpassword",
            database="mydb"
        )
        cursor = db.cursor()
        cursor.execute("SELECT msg FROM messages LIMIT 1;")
        msg = cursor.fetchone()[0]
        return jsonify({"message": msg})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

