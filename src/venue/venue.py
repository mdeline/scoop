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
    # Venue info
    result = db.session.execute(
        'select * from scoop.venue '
        + 'where id = :venue_id',
        {'venue_id': venue_id}
    )
    venue = result.fetchone()

    # Review count & review average
    result = db.session.execute(
        'select avg(stars)::numeric(3,2) as review_avg, '
        + 'count(stars) as review_count '
        + 'from scoop.review '
        + 'where venue_id = :venue_id',
        {'venue_id': venue_id}
    )
    review_aggregates = result.fetchone()

    # Reviews
    result = db.session.execute(
        'select review, stars, appuser.fullname as user, created_at '
        + 'from review '
        + 'inner join scoop.appuser on scoop.appuser.id = scoop.review.appuser_id '
        + 'where venue_id = :venue_id '
        + 'order by created_at desc',
        {'venue_id':venue_id})
    reviews = result.fetchall()

    return render_template(
        'venue.jinja2',
        venue=venue,
        review_aggregates=review_aggregates,
        reviews=reviews
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