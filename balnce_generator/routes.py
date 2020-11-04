from flask import render_template


@app.route("/capturadedatos', methods=['GET', 'POST']")
def capturadedatos():
    return render_template("captura.html", title="Captura de datos")
