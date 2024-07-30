from flask import Flask, request, make_response, request, flash, render_template
import string

app = Flask(__name__)

name_holder = []
name_holder.append("<p>This is a test to see that something shows up<p>")


@app.route("/")
def myform():
    return render_template("input_test.html")


@app.route('/', methods=["POST"])
def my_form_post():
    text = request.form['name']
    greetings = "Hello, " + string.capwords(text)

    return render_template("input_test.html", greetings=greetings)
