from flask_app import app
from flask import session, request, redirect, render_template, flash
from flask_app.models.recipe import Recipe

@app.route("/recipe/new")
def create_recipe():
    if "user_id" not in session:
        return redirect("/logout")
    return render_template("new_recipe.html", userid=session["user_id"])

@app.route("/new/recipe", methods=["POST"])
def created_recipe():
    if "user_id" not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect("/recipe/new")
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["inst"],
        "date_made": request.form["date_made"],
        "under_30": request.form["under_30"],
        "user_id": session["user_id"]
    }
    Recipe.save_recipe(data)
    return redirect("/dashboard")

@app.route("/recipe/<int:id>")
def view_recipe(id):
    recipe= Recipe.get_recipe_by_id(id)
    return render_template("view_recipe.html", recipe=recipe, username=session["first_name"])