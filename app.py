import os
import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # Get MySQL credentials from environment variables
    mysql_host = os.getenv('MYSQL_HOST')
    mysql_user = os.getenv('MYSQL_USER')
    mysql_password = os.getenv('MYSQL_PASSWORD')
    mysql_db = os.getenv('MYSQL_DB')
    
    # Connect to the MySQL RDS instance
    conn = mysql.connector.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        database=mysql_db
    )
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    
    # Return the data in JSON format
    return jsonify(rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
