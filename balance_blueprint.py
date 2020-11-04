from flask import Blueprint, render_template

balance = Blueprint("balance", __name__, static_folder="static", template_folder="templates")


@balance.route("/capturadedatos")
@balance.route("/")
def capturadedatos():
    render_template("capturadedatos.html")

