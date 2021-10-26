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

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
AGES = [
        "2-4",
        "4-6",
        "6+"]


@app.route("/get_walks")
def get_walks():
    """
    Get the walks from the database
    """
    walks = list(mongo.db.walks.find())
    return render_template("walks.html", walks=walks)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    walks = list(mongo.db.walks.find({"$text": {"$search": query}}))
    return render_template("walks.html", walks = walks)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already in use")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # get user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check username is in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check hashed password matches user input
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}!".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # if password does not match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't existing
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You are now logged out!")
    session.clear()
    return redirect(url_for("login"))


@app.route("/add_walk", methods=["GET", "POST"])
def add_walk():
    
    if request.method == "POST":
        walk = {
            "category_name": request.form.get("category_name"),
            "walk_title": request.form.get("walk_title"),
            "walk_description": request.form.get("walk_description"),
            "walk_facilities": list(request.form.getlist("walk_facilities")),
            "walk_length": request.form.get("walk_length"),
            "walk_age": request.form.get("walk_age"),
            "walk_image": request.form.get("walk_image"),
            "shared_by": session["user"]
        }
        mongo.db.walks.insert_one(walk)
        flash("You successfully added a walk!")
        return redirect("get_walks")

    categories = mongo.db.categories.find().sort("category_name", 1)
    facilities = mongo.db.facilities.find().sort("walk_facilities", 1)
    return render_template(
        "add_walk.html", categories=categories, ages=AGES,
        facilities=facilities)


@app.route("/edit_walk/<walk_id>", methods=["GET", "POST"])
def edit_walk(walk_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "walk_title": request.form.get("walk_title"),
            "walk_description": request.form.get("walk_description"),
            "walk_facilities": list(request.form.getlist("walk_facilities")),
            "walk_length": request.form.get("walk_length"),
            "walk_age": request.form.get("walk_age"),
            "walk_image": request.form.get("walk_image"),
            "shared_by": session["user"]
        }
        mongo.db.walks.update(
            {"_id": ObjectId(walk_id)}, {"$set": submit})
        flash("Walk Successfully Updated")

    walk = mongo.db.walks.find_one({"_id": ObjectId(walk_id)})
    facilities = mongo.db.facilities.find().sort("walk_facilities", 1)
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_walk.html", categories=categories, walk=walk,
        facilities=facilities, ages=AGES)


@app.route("/delete_walk/<walk_id>")
def delete_walk(walk_id):
    mongo.db.walks.remove({"_id": ObjectId(walk_id)})
    flash("Walk Deleted Successfully")
    return redirect(url_for("get_walks"))


@app.route("/view_walk/<walk_id>")
def view_walk(walk_id):
    walk = mongo.db.walks.find_one({"_id": ObjectId(walk_id)})
    user = mongo.db.users.find_one({"username": walk["shared_by"]})
    walks = mongo.db.walks.find()

    return render_template(
        "view_walk.html", walk=walk, user=user, walks=walks)


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name"),
            "category_image": request.form.get("category_image")
        }
        
        mongo.db.categories.insert_one(category)
        flash("Category Added!")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "category_image": request.form.get("category_image")
        }
        if request.files["image_file"].filename == "":
            submit["category_image"] = "https://en.wikipedia.org/wiki/Smiley#/media/File:SNice.svg"
        mongo.db.categories.update(
            {"_id": ObjectId(category_id)}, submit)
        flash("Category Updated!")

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):

    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Deleted Successfully")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
