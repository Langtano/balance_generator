from flask import Flask, render_template

app = Flask(__name__)


@app.route('/capturadedatos', methods=['GET', 'POST'])
def capturadedatos():
    return render_template(captura.html)


if __name__ == '__main__':
    app.run()
