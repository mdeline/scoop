from flask import Blueprint, render_template, request, redirect, url_for, session
from ..forms import ReviewForm
from .. import db

home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@home_bp.route("/", methods=["GET"])
def home():
    result = db.session.execute('select * from category')
    categories = result.fetchall()
    return render_template(
        "home.jinja2",
        template = "home-template",
        categories = categories
    )

@home_bp.route('/category/<category_id>', methods=['GET'])
def restaurantsByCategory(category_id):
     # Selected category's restaurants
    result = db.session.execute(
        'select * from restaurant '
        + 'inner join restaurantcategory rc on rc.restaurant_id = restaurant.id '
        + 'where rc.category_id = :category_id '
        + 'order by restaurant.name desc',
        {'category_id':category_id})

    restaurants = result.fetchall()

    return render_template(
        'category.jinja2',
        restaurants=restaurants,
    )

@home_bp.route("/result")
def result():
    query = request.args["query"].lower()
    sql =   ("SELECT * FROM restaurant "
            + "WHERE lower(street_address) LIKE :query "
            + "OR postal_code LIKE :query "
            + "OR lower(city) LIKE :query " 
            + "OR lower(neighbourhood) LIKE :query"
            )
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    restaurants = result.fetchall()
    return render_template(
        "result.jinja2", 
        restaurants=restaurants
    )