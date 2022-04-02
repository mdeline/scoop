from flask import Blueprint, render_template
from .. import db

home_bp = Blueprint(
    "home_bp", __name__,
    template_folder="templates",
    static_folder="static"
)

@home_bp.route("/", methods=["GET"])
def home():
    return render_template(
        "home.html",
        template = "home-template"
    )

@home_bp.route("/error", methods=["GET"])
def error():
    return render_template(
        "error.html",
        template = "error-template"
    )