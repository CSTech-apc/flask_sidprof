from flask import Flask, render_template
from app.ext import config


app = Flask(__name__)
config.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")
