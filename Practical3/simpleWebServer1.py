# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to My Web Server</h1><p>This is a static page</p>"

if __name__ == "__main__":
    app.run(debug=True)
