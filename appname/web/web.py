from . import web_bp
from flask import render_template

# Home page
@web_bp.route("/index")
def index():
    data = "hello world"
    return render_template("web/index.html", page_title="Home Page", data=data)


# About page
@web_bp.route("/about")
def login():
    data = "login"
    return render_template("web/about.html", page_title="About", data=data)
