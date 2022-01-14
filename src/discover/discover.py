from flask import Blueprint, render_template
from .. import db

discover_pb = Blueprint(
    'discover_pb', __name__,
    template_folder='templates',
    static_folder='static'
)

@discover_pb.route('/discover', methods=['GET'])
def discover():
    result = db.session.execute('SELECT * FROM restaurant')
    restaurants = result.fetchall()
    return render_template(
        'discover.jinja2',
        restaurants=restaurants
    )