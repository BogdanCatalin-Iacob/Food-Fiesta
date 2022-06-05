from flask import render_template
from food_fiesta import app, db
from food_fiesta.models import Category, Users


@app.route("/")
def home():
    '''
    render the base.html page
    '''
    return render_template("recipes.html")


@app.route("/categories")
def categories():
    '''
    render the categories.html page
    '''
    return render_template("categories.html")


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    '''
    render the add_category.html page
    '''
    return render_template("add_category.html")
