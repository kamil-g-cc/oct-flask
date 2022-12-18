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
    text_to_show = "Testuje <i>przekazywanie</i> zmiennej do Jinja"
    items = [{"content": "Onet.pl", "url": "https://onet.pl"}, {"content":"GOOGLE", "url": "https://google.com"}]
    return render_template("thanks.html", welcome=text_to_show, list_to_iterate=items)