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

    page_length = request.form['page_length']
    current_page = request.form['current_page']

    progress_calculation = int(page_length) - int(current_page)
    progress = "You have " + str(progress_calculation) + " pages to go"

    return render_template("input_test.html", greetings=greetings, progress=progress)
