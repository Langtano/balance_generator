from flask import Flask


app = Flask(__name__)

from balnce_generator import routes
