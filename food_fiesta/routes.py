from flask import render_template, request, redirect, url_for, flash, session
from food_fiesta import app, db
from werkzeug.security import generate_password_hash, check_password_hash
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
    render the categories from db on categories.html page
    '''
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


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


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    '''
    edit a category name and save on db
    '''
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    '''
    delete the category based on category id
    if delete button is clicked
    '''
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


@app.route("/register", methods=["GET", "POST"])
def register():
    '''
    add a new user to db
    if the user already exists, a flash message will be prompted
    and register page will be displayed
    '''

    if request.method == "POST":
        # check if username exists in db
        user_exists = Users.query.filter(
            Users.user_name == request.form.get("user_name").lower()).all()

        if user_exists:
            flash("Username already exists")
            return redirect(url_for("register"))

        # check if the password matches confirm_password
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        if password == confirm_password:
            user = Users(
                user_name=request.form.get("user_name").lower(),
                password=generate_password_hash(request.form.get("password"))
            )

            db.session.add(user)
            db.session.commit()

            # put new user in session cookie
            session["user"] = request.form.get("user_name").lower()
            flash("Registration successful!")
            return redirect(url_for("profile", user_name=session["user"]))
        else:
            flash("Password does not match!")

    return render_template("register.html")
