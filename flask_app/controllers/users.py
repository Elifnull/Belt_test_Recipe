from flask_app import app
from flask import session, request, redirect, render_template, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_user", methods=["POST"])
def create_user():
    if not User.validate_reg(request.form):
        return redirect("/")
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password":bcrypt.generate_password_hash(request.form['password'])
    }
    User.save_user(data)
    account = User.get_with_email(request.form["email"])
    session["user_id"] = account.id
    session["first_name"] = account.first_name
    print(account.id)
    return redirect("/dashboard")

@app.route("/login", methods=["POST"])
def login():
    pass

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect('/logout')
    first_name = session["first_name"]
    recipes_all = Recipe.get_all_recipe
    return render_template("dashboard.html", username= first_name, userid = session["user_id"], all_recipes = recipes_all)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')