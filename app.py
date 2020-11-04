from flask import Flask
from balance_blueprint import balance

app = Flask(__name__)


if __name__ == '__main__':
    app.run()
