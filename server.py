#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timezone
from flask import Flask, request, render_template, jsonify

app = Flask(__name__, static_folder="public", template_folder="views")

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/api/hello")
def hello():
    return jsonify(greeting="Hello, API")

@app.route("/api/fileanalyse", methods=["POST"])
def fileanalyse():
    file = request.files["upfile"]
    blob = file.read()
    return jsonify(name=file.filename,
                   size=len(blob))
        
if __name__ == "__main__":
    app.run()
