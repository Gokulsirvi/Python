# app.py
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def form():
    return '''
    <form method="post" action="/process">
    Enter Name: <input name="name"><br>
    <input type="submit">
    </form>
    '''

@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    return f"Hello, {name}! Data received successfully."

if __name__ == "__main__":
    app.run(debug=True)
