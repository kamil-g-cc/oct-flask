from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/note", methods=["POST", "GET"])
def add_note():
    if request.method == "POST":
        print("data from request: ", request.form.get("name"), request.form.get("note"))
        return redirect("/thanks")
    elif request.method == "GET":
        return "This supose to be a form"
    return redirect("/thanks")

@app.route("/thanks")
def thank_you():
    return "Thank you for submitting the note"