from flask import Blueprint, render_template, request, redirect, url_for, session
from ..forms import ReviewForm
from .. import db

venue_bp = Blueprint(
    'venue_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@venue_bp.route('/venue/<venue_id>', methods=['GET'])
def venue(venue_id):
    # List restaurant information
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

@venue_bp.route('/venue/review', methods=['POST'])
def review():
    form = ReviewForm()
    venue_id = request.form["venue_id"]
    #todo: use form validation
    sql = 'insert into scoop.review(review, stars, appuser_id, venue_id) values(:review, 3, :appuser_id, :venue_id)'
    db.session.execute(sql, {
        'review': form.review.data,
        'appuser_id': session["appuser_id"],
        'venue_id': venue_id
    })
    db.session.commit()
    return redirect(url_for("venue_bp.venue", venue_id=venue_id))


