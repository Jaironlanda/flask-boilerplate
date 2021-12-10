from . import user_bp
from flask import render_template


@user_bp.route("/dashboard")
def dashboard():
    return render_template("user/dashboard.html", data="dashboard data")


@user_bp.route("/profile")
def profile():
    return render_template("user/profile.html", data="profile data")
