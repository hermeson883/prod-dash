from flask import Flask, render_template

not_found = Flask(__name__)

@not_found.errorhandler(404)
def page_not_found(e):
    return render_template("not_found.html")