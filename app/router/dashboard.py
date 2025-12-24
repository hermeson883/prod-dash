from flask import Blueprint

dash_bp = Blueprint("dashboard", __name__)

@dash_bp.route("/dashboard")
def dashboard():
    return "dashboard"
