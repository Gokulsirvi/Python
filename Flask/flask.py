# ---------------------------------------------------------
# IMPORTS
# ---------------------------------------------------------
from flask import Flask, render_template_string, request, jsonify, redirect, url_for
import sqlite3   # database

# Create Flask app
app = Flask(__name__)


# ---------------------------------------------------------
# DATABASE SETUP (SQLite)
# ---------------------------------------------------------
def create_db():
    """Creates database and table if not exists."""
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    
    # Create table
    c.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    """)
    
    conn.commit()
    conn.close()

# Run DB setup once
create_db()


# ---------------------------------------------------------
# HOME PAGE ROUTE
# ---------------------------------------------------------
@app.route("/")
def home():
    return """
        <h1>Welcome to Flask One-Page Project</h1>
        <p>Try routes:</p>
        <ul>
            <li>/hello/yourname</li>
            <li>/template</li>
            <li>/form</li>
            <li>/users</li>
            <li>/api/data</li>
        </ul>
    """


# ---------------------------------------------------------
# SIMPLE ROUTE WITH URL PARAMETER
# ---------------------------------------------------------
@app.route("/hello/<name>")
def hello(name):
    """Shows dynamic text using URL parameter."""
    return f"<h2>Hello {name}!</h2>"


# ---------------------------------------------------------
# TEMPLATE RENDERING (No separate HTML file required)
# ---------------------------------------------------------
@app.route("/template")
def template_page():
    """Renders template using string (render_template_string)."""
    html = """
        <h2>Template Example</h2>
        <p>Welcome, {{ username }}!</p>
    """
    return render_template_string(html, username="Gokul")


# ---------------------------------------------------------
# FORM PAGE (GET + POST)
# ---------------------------------------------------------
@app.route("/form", methods=["GET", "POST"])
def form():
    """Handles form submission and saves data into database."""
    
    if request.method == "POST":
        # Get input values
        name = request.form["name"]
        email = request.form["email"]

        # Save to database
        conn = sqlite3.connect("data.db")
        c = conn.cursor()
        c.execute("INSERT INTO users(name, email) VALUES(?, ?)", (name, email))
        conn.commit()
        conn.close()

        # redirect to users page
        return redirect(url_for("users"))

    # HTML form
    form_html = """
        <h2>User Form</h2>
        <form method="POST">
            <input name="name" placeholder="Enter Name"><br><br>
            <input name="email" placeholder="Enter Email"><br><br>
            <button type="submit">Submit</button>
        </form>
    """
    return form_html


# ---------------------------------------------------------
# SHOW DATA FROM DATABASE
# ---------------------------------------------------------
@app.route("/users")
def users():
    """Fetches all users from database and displays them."""
    
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    data = c.fetchall()
    conn.close()

    html = "<h2>Users List</h2>"
    for row in data:
        html += f"<p>ID: {row[0]} | Name: {row[1]} | Email: {row[2]}</p>"

    return html


# ---------------------------------------------------------
# JSON API ENDPOINT
# ---------------------------------------------------------
@app.route("/api/data")
def api_data():
    """Returns JSON data."""
    return jsonify({
        "status": "success",
        "message": "This is sample API data",
        "users_example": ["user1", "user2"]
    })


# ---------------------------------------------------------
# ERROR HANDLING
# ---------------------------------------------------------
@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error page."""
    return "<h1>404 - Page Not Found</h1>", 404


# ---------------------------------------------------------
# RUN SERVER
# ---------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
