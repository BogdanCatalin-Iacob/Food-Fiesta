from flask import render_template, request, redirect, url_for
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
    add a created category into database
    '''
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")
