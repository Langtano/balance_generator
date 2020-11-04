from flask import Flask
from balance_blueprint import balance

app = Flask(__name__)
app.register_blueprint(balance, url_prefix="")

if __name__ == '__main__':
    app.run()
