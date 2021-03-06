import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# Config #
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Home page
@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    # Shows the recipes #
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    # Allow users to search recipes
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


# Allow users to register on the website
@app.route("/register", methods=["GET", "POST"])
def register():
    # check if the user is logged in and don't allow them to register again
    if "user" in session:
        return redirect("error_handlers/403.html")

    if request.method == "POST":
        # check if the username is already registered in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into a 'session' cookie on website
        session["user"] = request.form.get("username").lower()
        flash("Welcome, Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# Allow users to login
@app.route("/login", methods=["GET", "POST"])
def login():
    # check if the user is logged in and don't allow them to login again
    if "user" in session:
        return redirect("error_handlers/403.html")

    if request.method == "POST":
        # check to see of username is in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure the password matches the one in the database
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome to Keto 4 Me {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # when the password doesn't match
                flash("Your password and/or Username is incorrect")
                return redirect(url_for("login"))

        else:
            # If the username does not exist
            flash("Your password and/or Username is incorrect")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Only users can access profile
    if not session.get("user"):
        return render_template("error_handlers/403.html")

    # getting the session's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        # Admin has access to all recipes
        if session["user"] == "admin":
            user_recipes = list(mongo.db.recipes.find())
        else:
            # user sees own recipes
            user_recipes = list(
                mongo.db.recipes.find({"created_by": session["user"]}))
        return render_template(
            "profile.html", username=username, user_recipes=user_recipes)
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Allowing a user to log out of the website
    flash("You have been Logged Out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    # Only users can add recipes
    if not session.get("user"):
        return render_template("error_handlers/403.html")

    # Allow users to add recipes to the website
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "image_url": request.form.get("image_url"),
            "serves": request.form.get("serves"),
            "prep_time": request.form.get("prep_time"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Your recipe has been Sumitted, Thank You!")
        return redirect(url_for('get_recipes'))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    # Only users can edit recipes
    if not session.get("user"):
        return render_template("error_handlers/403.html")

    # Allow users to edit their recipes
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "image_url": request.form.get("image_url"),
            "serves": request.form.get("serves"),
            "prep_time": request.form.get("prep_time"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Your recipe has been Edited and Updated, Thank You!")
        return redirect(url_for('get_recipes'))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)


@app.route("/delete_recipe<recipe_id>")
def delete_recipe(recipe_id):
    # Only users can delete their own recipes
    if not session.get("user"):
        return render_template("error_handlers/403.html")

    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Your recipe has successfully been deleted")
    return redirect(url_for('get_recipes'))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    # Only admin can access categories
    if not session.get("user") == "admin":
        return render_template("error_handlers/403.html")

    # allow admin to create new categories
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("You've added a new category")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    # allow admin to edit the categories
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("You have successfully updated the category")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    # allow admin to delete categories
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("You have successfully deleted the category")
    return redirect(url_for("get_categories"))


# Error Handlers #
@app.errorhandler(404)
def not_found(e):
    return render_template("error_handlers/404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("error_handlers/500.html"), 500


@app.errorhandler(403)
def forbidden(e):
    return render_template("error_handlers/403.html"), 403

# Running the website #
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
