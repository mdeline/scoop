from flask import Blueprint, render_template, request
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

@home_bp.route("/result")
def result():
    query = request.args["query"].lower()
    sql =   ("SELECT * FROM restaurant "
            + "WHERE lower(address) LIKE :query "
            + "OR postalcode LIKE :query "
            + "OR lower(city) LIKE :query")
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    restaurants = result.fetchall()
    return render_template(
        "result.jinja2", 
        restaurants=restaurants
    )

@home_bp.route('/restaurant/<restaurant_id>', methods=['GET'])
def restaurant(restaurant_id):

     # Restaurant
    result = db.session.execute(
        'select name from restaurant '
        + 'where id = :id',
        {'id':restaurant_id})
    restaurant = result.fetchone()

    # Reviews
    result = db.session.execute(
        'select review, forks, scoop.user.name as user from review '
        + 'inner join scoop.user on scoop.user.id = review.user_id '
        + 'where restaurant_id = :id '
        + 'order by created_at desc',
        {'id':restaurant_id})
    reviews = result.fetchall()

    return render_template(
        'restaurant.jinja2',
        restaurant=restaurant,
        reviews=reviews
    )

