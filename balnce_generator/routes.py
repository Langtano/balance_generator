from balnce_generator import app

from flask import render_template



@app.route('/')
def index():
    return "Hello"


@app.route("/capturadedatos")
def capturadedatos():
    return render_template("captura.html")
