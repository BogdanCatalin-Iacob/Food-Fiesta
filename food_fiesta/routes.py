from flask import render_template
from food_fiesta import app, db


@app.route("/")
def home():
    '''
    render the base.html page
    '''
    return render_template("base.html")
