from flask import Blueprint, render_template

login_router = Blueprint("login", __name__)

@login_router.route("/")
def login():
    return render_template("login.html")