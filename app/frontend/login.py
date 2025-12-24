from flask import Flask
from router.dashboard import dash_bp
from router.login import login_router
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__, 
    template_folder=os.path.join(BASE_DIR, "views"),
    static_folder=os.path.join(BASE_DIR, "assets")
)

app.register_blueprint(login_router)
app.register_blueprint(dash_bp)
