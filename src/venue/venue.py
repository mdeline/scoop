from flask import Blueprint, render_template, request, redirect, url_for, session
from ..forms import ReviewForm
from .. import db

venue_bp = Blueprint(
    'venue_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@venue_bp.route('/<venue_id>', methods=['GET'])
def venue(venue_id):
    # List restaurant information
    url_prefix=venue_bp.name
    print(url_prefix)

    result = db.session.execute(
        'select id, name from scoop.venue '
        + 'where id = :venue_id',
        {'venue_id':venue_id})
    venue = result.fetchone()

    # Reviews
    result = db.session.execute(
        'select review, stars, appuser.fullname as user from review '
        + 'inner join scoop.appuser on scoop.appuser.id = scoop.review.appuser_id '
        + 'where venue_id = :venue_id '
        + 'order by created_at desc',
        {'venue_id':venue_id})
    reviews = result.fetchall()

    # Form
    form = ReviewForm()

    return render_template(
        'venue.jinja2',
        venue=venue,
        reviews=reviews,
        form=form
    )

@venue_bp.route('/review', methods=['POST'])
def review():
    review = request.form["review"]
    rating = request.form["rating"]
    appuser_id = session["appuser_id"]
    venue_id = request.form["venue_id"]
    
    #todo: use form validation
    sql = 'insert into scoop.review(review, stars, appuser_id, venue_id) values(:review, :rating, :appuser_id, :venue_id)'
    db.session.execute(sql, {
        'review': review,
        'rating': rating,
        'appuser_id': appuser_id,
        'venue_id': venue_id,
        
    })
    db.session.commit()
    return redirect(url_for("venue_bp.venue", venue_id=venue_id))