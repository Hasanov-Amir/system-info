from flask import Flask, request, render_template

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


@app.route("/start-dir", methods=['POST', 'GET'])
def start_dir():
    if request.method == "POST":
        ctx = request.get_json()
        start = ctx.get("start", None)
        utils.START_DIR = start
        return {"response": f"Start dir was set to {utils.START_DIR}"}

    if param := request.query_string:
        param = param.decode().split("=")
        params = {
            param[0]: int(param[1])
        }

        if params.get("erase", False):
            utils.START_DIR = "C:\\"
            return {"response": f"start dir was set to {utils.START_DIR}"}

    return {"response": utils.START_DIR}
