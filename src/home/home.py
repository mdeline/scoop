from flask import Blueprint, render_template, request
from ..models import Restaurant, db

home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

result_bp = Blueprint(
    'result_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@home_bp.route("/", methods=["GET"])
def home():
    return render_template(
        "home.jinja2",
        template="home-template"
    )

@result_bp.route("/result")
def result():
    query = request.args["query"]
    sql = "SELECT name, description, address FROM restaurant WHERE address LIKE :query"
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    restaurants = result.fetchall()
    return render_template(
        "result.jinja2", 
        restaurants=restaurants
    )