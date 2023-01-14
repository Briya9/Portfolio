from flask_app.models import user
from flask import redirect, render_template, request, session
from flask_app import app


@app.route("/")
def root_route():
    return render_template("home_page.html")


@app.route("/about")
def about_page():
    return redirect("/")