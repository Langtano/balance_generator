from balnce_generator import app
from balnce_generator import form
from flask import render_template


@app.route('/')
def home():
    return "Charles, el mundo ya no es como antes"


@app.route("/capturadedatos")
def capturadedatos():
    registration_form = form.RegistrationForm('/capturadedatos')
    return render_template("capture.html", form=registration_form)
