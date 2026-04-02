from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# ---------- DATABASE ----------
def init_db():
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT,
            role TEXT,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# ---------- ROUTES ----------
@app.route('/')
def home():
    return "Backend running!"

@app.route('/add_job', methods=['POST'])
def add_job():
    data = request.json

    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute(
        "INSERT INTO jobs (company, role, status) VALUES (?, ?, ?)",
        (data['company'], data['role'], data['status'])
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Added"})

@app.route('/get_jobs', methods=['GET'])
def get_jobs():
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute("SELECT * FROM jobs")
    rows = c.fetchall()
    conn.close()

    jobs = []
    for row in rows:
        jobs.append({
            "id": row[0],
            "company": row[1],
            "role": row[2],
            "status": row[3]
        })

    return jsonify(jobs)

@app.route('/update_job/<int:id>', methods=['PUT'])
def update_job(id):
    data = request.json

    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute("UPDATE jobs SET status=? WHERE id=?", (data['status'], id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Updated"})

@app.route('/delete_job/<int:id>', methods=['DELETE'])
def delete_job(id):
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute("DELETE FROM jobs WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Deleted"})

# ---------- RUN ----------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)