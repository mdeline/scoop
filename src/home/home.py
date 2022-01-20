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

@home_bp.route('/restaurant/<restaurant_id>', methods=['GET'])
def restaurant(restaurant_id):
    # Restaurant
    result = db.session.execute(
        'select id, name from restaurant '
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

    # Form
    form = ReviewForm()

    return render_template(
        'restaurant.jinja2',
        restaurant=restaurant,
        reviews=reviews,
        form=form
    )

@home_bp.route('/review', methods=['POST'])
def review():
    form = ReviewForm()
    restaurant_id = request.form["restaurant_id"]
    #todo: use form validation
    sql = 'insert into scoop.review(review, forks, user_id, restaurant_id, created_at) values(:review, 3, :user_id, :restaurant_id, now())'
    db.session.execute(sql, {
        'review': form.review.data,
        'user_id': session["user_id"],
        'restaurant_id': restaurant_id
    })
    db.session.commit()
    return redirect(url_for("home_bp.restaurant", restaurant_id=restaurant_id))