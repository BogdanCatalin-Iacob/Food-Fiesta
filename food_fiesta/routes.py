'''
Creates the routes to pages.
Get / send data from / to db
'''

from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId   # render mongoDb docs by their unique id
from food_fiesta import app, db, mongo
from food_fiesta.models import Category, Users


@app.route("/")
def home():
    '''
    render the home.html page
    '''
    return render_template("home.html")


@app.route("/categories")
def categories():
    '''
    render the categories from db on categories.html page
    '''
    # check if user is logged in as admin
    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to edit Categories!")
        return redirect(url_for("get_recipes"))

    get_categories = list(
        Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=get_categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    '''
    add a created category into database
    '''
    # check if user is logged in as admin
    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to edit Categories!")
        return redirect(url_for("get_recipes"))

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
    # check if user is logged in as admin
    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to edit Categories!")
        return redirect(url_for("get_recipes"))

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
    # check if user is logged in as admin
    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to edit Categories!")
        return redirect(url_for("get_recipes"))

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
    '''
    display's profile page of the user in session
    '''
    # get the recipes from db to display the user's created recipes
    recipes = list(mongo.db.instructions.find())
    return render_template(
        "profile.html",
        user_name=session["user"].capitalize(),
        recipes=recipes)


@app.route("/get_recipes")
def get_recipes():
    '''
    get the recipes from mongodb
    '''
    recipes = list(mongo.db.instructions.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/create_recipe", methods=["GET", "POST"])
def create_recipe():
    '''
    create a recipe document and send it to mongo db
    '''
    # check if user is logged in
    if "user" not in session:
        flash("You have to be logged in to create a recipe")
        return redirect(url_for("get_recipes"))

    # get the available categories
    get_categories = list(
        Category.query.order_by(Category.category_name).all())

    if request.method == "POST":

        # create the document to be sent to db
        recipe = {
            "category_id": request.form.get("category_id"),
            "recipe_name": request.form.get("recipe_name"),
            "cook_time": request.form.get("cook_time"),
            "prep_time": request.form.get("prep_time"),
            "servings": request.form.get("servings"),
            "ingredients": request.form.getlist("ingredientsList"),
            "steps": request.form.getlist("stepsList"),
            "created_by": session["user"]
        }

        mongo.db.instructions.insert_one(recipe)
        flash("Recipe successfully saved")
        return redirect(url_for("get_recipes"))
    return render_template("create_recipe.html", categories=get_categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    '''
    edit the selected recipe and
    save changes into db
    '''
    recipe = mongo.db.instructions.find_one({"_id": ObjectId(recipe_id)})

    # recipes = list(mongo.db.instructions.find())
    categories = list(Category.query.order_by(Category.category_name).all())

    if request.method == "POST":

        # create the document to be sent to db
        submit_recipe = {
            "category_id": request.form.get("category_id"),
            "recipe_name": request.form.get("recipe_name"),
            "cook_time": request.form.get("cook_time"),
            "prep_time": request.form.get("prep_time"),
            "servings": request.form.get("servings"),
            "ingredients": request.form.getlist("ingredientsList"),
            "steps": request.form.getlist("stepsList"),
            "created_by": session["user"]
        }

        mongo.db.instructions.replace_one(
            {"_id": ObjectId(recipe_id)}, submit_recipe)
        flash("Recipe successfully updated")

    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    '''
    delete the selected recipe
    '''
    mongo.db.instructions.delete_one({"_id": ObjectId(recipe_id)})
    flash("Task successfully deleted")
    return redirect(url_for("get_recipes"))
