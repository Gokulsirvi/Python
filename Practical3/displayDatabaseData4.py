# app.py
from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def show_data():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER, name TEXT)")
    cursor.execute("INSERT INTO students VALUES(1, 'Aman')")
    cursor.execute("INSERT INTO students VALUES(2, 'Riya')")

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    html = "<table border=1><tr><th>ID</th><th>Name</th></tr>"
    for row in data:
        html += f"<tr><td>{row[0]}</td><td>{row[1]}</td></tr>"
    html += "</table>"

    conn.commit()
    conn.close()

    return html

if __name__ == "__main__":
    app.run(debug=True)
