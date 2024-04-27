from flask import Flask
from flask_bootstrap import Bootstrap

# def create_app(): # TODO: Factor this into its own function later, setting as a global var for now
app = Flask(__name__)
Bootstrap(app)
# return app

@app.route("/")
def hello_world():
    return '<h1>Hello world</h1>'
    # return render_template('base.html') # TODO still working on this