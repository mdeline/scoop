from flask import Blueprint, render_template, request, redirect, url_for, session
from .. import db

home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@home_bp.route("/", methods=["GET"])
def home():
    return render_template(
        "home.jinja2",
        template = "home-template"
    )

@home_bp.route("/result")
def result():
    query = request.args["query"].lower()
    sql =   ("select * from scoop.venue "
            + "where lower(street_address) like :query "
            + "or postal_code like :query "
            + "or lower(city) like :query " 
            + "or lower(neighbourhood) like :query"
            )
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    venues = result.fetchall()
    return render_template(
        "result.jinja2", 
        venues=venues
    )