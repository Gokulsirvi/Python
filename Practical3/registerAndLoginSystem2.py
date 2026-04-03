# app.py
from flask import Flask, request

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return '''
    <h2>Register</h2>
    <form method="post" action="/register">
    Username: <input name="username"><br>
    Password: <input name="password"><br>
    <input type="submit">
    </form>

    <h2>Login</h2>
    <form method="post" action="/login">
    Username: <input name="username"><br>
    Password: <input name="password"><br>
    <input type="submit">
    </form>
    '''

@app.route("/register", methods=["POST"])
def register():
    users[request.form["username"]] = request.form["password"]
    return "Registered Successfully"

@app.route("/login", methods=["POST"])
def login():
    u = request.form["username"]
    p = request.form["password"]

    if users.get(u) == p:
        return "Login Successful"
    else:
        return "Invalid Credentials"

if __name__ == "__main__":
    app.run(debug=True)
