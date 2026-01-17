import os
import pymysql
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# MySQL configuration
MYSQL_HOST = os.environ.get('MYSQL_HOST', 'mysql')
MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'root')
MYSQL_DB = os.environ.get('MYSQL_DB', 'devops')

def get_db_connection():
    return pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB,
        cursorclass=pymysql.cursors.Cursor
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT message FROM messages")
    messages = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', messages=messages)

@app.route('/submit', methods=['POST'])
def submit():
    new_message = request.form.get('new_message')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO messages (message) VALUES (%s)", (new_message,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": new_message})

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
