from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name', '')
    gender = data.get('gender', '')
    birthday = data.get('birthday', '')
    phone = data.get('phone', '')
    note = data.get('note', '')

    conn = sqlite3.connect('visitors.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS visitors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            gender TEXT,
            birthday TEXT,
            phone TEXT,
            note TEXT
        )
    """)
    cursor.execute('INSERT INTO visitors (name, gender, birthday, phone, note) VALUES (?, ?, ?, ?, ?)',
                   (name, gender, birthday, phone, note))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
