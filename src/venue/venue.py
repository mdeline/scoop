from flask import Blueprint, render_template, request, redirect, url_for, session
from .. import db

venue_bp = Blueprint(
    'venue_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@venue_bp.route('/<venue_id>', methods=['GET'])
def venue(venue_id):
    # Venue info
    venue = db.session.execute(
        'select * from scoop.venue '
        + 'where id = :venue_id',
        {'venue_id': venue_id}
    ).fetchone()

    # Review count & review average
    review_aggregates = db.session.execute(
        'select '
        + 'coalesce(avg(stars)::numeric(3,2), 0) as review_avg, '
        + 'coalesce(count(review), 0) as review_count '
        + 'from scoop.review '
        + 'where venue_id = :venue_id',
        {'venue_id': venue_id}
    ).fetchone()

    # Reviews
    reviews = db.session.execute(
        'select review.id, review, stars, appuser.fullname as user, '
        + 'appuser_id, created_at, modified_at, img_url as user_photo from review '
        + 'inner join scoop.appuser on scoop.appuser.id = scoop.review.appuser_id '
        + 'where venue_id = :venue_id '
        + 'order by created_at desc '
        + 'limit 10',
        {'venue_id':venue_id}
    ).fetchall()

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

@venue_bp.route('/<venue_id>/review/<review_id>', methods=['GET'])
def get_review(venue_id, review_id):
    review = db.session.execute(
        'select * from review where id = :review_id',
        {'review_id': review_id}
    ).fetchone()

    return render_template(
        'edit_review.jinja2',
        review=review
    )

@venue_bp.route('/<venue_id>/review/<review_id>', methods=['POST'])
def edit_review(venue_id, review_id):
    review = request.form["review"]
    rating = request.form["rating"]

    db.session.execute(
        'update review set review = :review, stars = :stars, modified_at = now() '
        + 'where id = :review_id',
        {
            'review': review,
            'stars': rating,
            'review_id': review_id
        }
    )
    db.session.commit()
    return redirect(url_for("venue_bp.venue", venue_id=venue_id))