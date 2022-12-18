from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/note")
def add_note():
    print("data from request: ", request.args.get["name"], request.args.get("note"))
    return "OK"

