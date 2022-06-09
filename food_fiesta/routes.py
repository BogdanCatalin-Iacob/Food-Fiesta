from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from food_fiesta import app, db, mongo
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
        if password != confirm_password:
            flash("Password does not match!")
            return redirect(url_for("register"))

        # get user info from the form
        user = Users(
            user_name=request.form.get("user_name").lower(),
            password=generate_password_hash(request.form.get("password")),
            email=request.form.get("email"),
            is_superuser=False
            )

        # send user info to db
        db.session.add(user)
        db.session.commit()

        # put new user in session cookie
        session["user"] = request.form.get("user_name").lower()
        flash("Registration successful!")
        return redirect(url_for("profile", user_name=session["user"]))

    return render_template("register.html")


# @app.route("/profile/<user_name>", methods=["GET", "POST"])
# def profile(user_name):
#     '''
#     check if the user is logged in and display profile.html
#     '''
#     if "user" in session:
#         return render_template("profile.html")

#     return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    '''
    log the user in if the username exists in db
    and the password matches
    '''
    if request.method == "POST":
        # check if username exists in db
        user_exists = Users.query.filter(
            Users.user_name == request.form.get("user_name").lower()).all()

        if user_exists:
            # check if password matches with the password in db
            if check_password_hash(
                        user_exists[0].password, request.form.get("password")):
                session["user"] = request.form.get("user_name").lower()

                flash(f"Welcome, {request.form.get('user_name').capitalize()}")
                return redirect(
                    url_for("profile", user_name=session["user"].capitalize()))
        
        # if wrong username or password
        flash("Wrong username and/or password")
        return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    '''
    log out the user from current session
    '''
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/profile")
def profile():
    return render_template("profile.html", user_name=session["user"].capitalize())


@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.instructions.find())
    print(recipes)
    return render_template("recipes.html", recipes=recipes)


@app.route("/create_recipe", methods=["GET", "POST"])
def create_recipe():
    total_time = 0
    return render_template("create_recipe.html", total_time=total_time)
