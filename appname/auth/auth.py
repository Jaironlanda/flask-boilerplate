from . import auth_bp
from flask import render_template


@auth_bp.route("/login")
def login():
    return render_template("auth/login.html", page_title="Login", data="login auth")


@auth_bp.route("/register")
def register():
    return render_template(
        "auth/register.html", page_title="Register", data="register page"
    )


@auth_bp.route("/forgot_pswd")
def forgot_pswd():
    return render_template(
        "auth/forgot_pswd.html", page_title="Forgot password", data="forgot password"
    )
