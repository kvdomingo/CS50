import requests
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():
    currency = request.form.get("currency")
    res = requests.get("http://data.fixer.io/api/latest?access_key=70ae574887f99c29be8759108396733a", params={"symbols": currency})

    if res.status_code != 200:
        return jsonify({"success": False})

    data = res.json()
    if currency not in data["rates"]:
        return jsonify({"success": False})

    return jsonify({"success": True, "rate": data["rates"][currency]})