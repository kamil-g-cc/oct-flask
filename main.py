from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/note", methods=["POST"])
def add_note():
    #print("data from request: ", request.args.get["name"], request.args.get("note"))
    print("data from request: ", request.form.get("name"), request.form.get("note"))
    return "OK, " + request.form.get("name") + ". Dziękuję za Twoją notatkę o treści: " + request.form.get("note")

