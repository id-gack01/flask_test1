So in a directory of your choice, run...

git https://github.com/id-gack01/flask_test1.git

You can substitute for whatever name you wanna give that project

For Linux
$ mkdir testapp 
$ cd testapp
$ python3 -m venv .venv (for Windows, write "py -3 -m venv .venv" instead for the final line)

$ . .venv/bin/activate (for Windows, write " .venv\Scripts\activate")

cd to that activated environment and install Flask and some other packages 

$ pip install Flask MarkupSafe Werkzeug blinker Jinja2 itsdangerous

To run, type the following command...

$ flask --app test_app.py run 
