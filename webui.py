from flask import Flask
from flask import render_template

import utils

# app object
app = Flask(__name__)


# main page
@app.route("/")
def index():
    return render_template("home.html")


# url for requesting utils by name For Ex.: installed_apps
@app.route("/<name>")
def get_util(name):
    result = None

    # check name for existence in list of utils
    if name in utils.__all__:
        result = eval(f"utils.{name}()")

    response = {
        "res": result
    }

    return response  # JSON
