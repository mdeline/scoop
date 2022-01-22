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
def venuesByCategory(category_id):
     # Selected category's venues
    result = db.session.execute(
        'select * from scoop.venue '
        + 'inner join scoop.venuecategory vc on vc.venue_id = venue.id '
        + 'where vc.category_id = :category_id '
        + 'order by venue.name desc',
        {'category_id':category_id})

    venues = result.fetchall()

    return render_template(
        'category.jinja2',
        venues=venues,
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