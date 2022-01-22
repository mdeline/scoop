from flask import Blueprint, render_template, request, redirect, url_for, session
from ..forms import ReviewForm
from .. import db

venue_bp = Blueprint(
    'venue_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@venue_bp.route('/restaurant/<restaurant_id>', methods=['GET'])
def restaurant(restaurant_id):
    # List restaurant information
    result = db.session.execute(
        'select id, name from restaurant '
        + 'where id = :restaurant_id',
        {'restaurant_id':restaurant_id})
    restaurant = result.fetchone()

    # Reviews
    result = db.session.execute(
        'select review, forks, scoop.user.name as user from review '
        + 'inner join scoop.user on scoop.user.id = review.user_id '
        + 'where restaurant_id = :restaurant_id '
        + 'order by created_at desc',
        {'restaurant_id':restaurant_id})
    reviews = result.fetchall()

    # Form
    form = ReviewForm()

    return render_template(
        'restaurant.jinja2',
        restaurant=restaurant,
        reviews=reviews,
        form=form
    )

@venue_bp.route('/restaurant/review', methods=['POST'])
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
    return redirect(url_for("venue_bp.restaurant", restaurant_id=restaurant_id))


