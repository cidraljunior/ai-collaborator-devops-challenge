# app.py
from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_NAME = os.environ.get('DB_NAME', 'customerdb')
DB_USER = os.environ.get('DB_USER', 'app_user')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')
DB_PORT = os.environ.get('DB_PORT', '5432')

@app.route('/')
def index():
    return 'Hello from app-microservice!'

@app.route('/db-test')
def db_test():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        cur = conn.cursor()
        # Perform a simple query
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({'db_version': db_version[0]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
