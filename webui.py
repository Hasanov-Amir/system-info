from flask import Flask
from flask import render_template

import utils

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/<name>")
def get_util(name):
    result = None
    if name in utils.__all__:
        result = eval(f"utils.{name}()")
    response = {
        "res": result
    }
    return response
