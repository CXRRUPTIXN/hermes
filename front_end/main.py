from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# def create_app(): # TODO: Factor this into its own function later, setting as a global var for now
app = Flask(__name__)
# return app

@app.route("/")
def hello_world():
    return render_template('base.html')