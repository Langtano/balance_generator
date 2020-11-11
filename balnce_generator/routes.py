from flask import render_template
from balnce_generator import app

@app.route("/capturadedatos', methods=['GET', 'POST']")
def capturadedatos():
    return render_template("captura.html", title="Captura de datos")
