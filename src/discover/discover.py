from flask import Blueprint, render_template, request, redirect, url_for, session
from .. import db

discover_pb = Blueprint(
    'discover_pb', __name__,
    template_folder='templates',
    static_folder='static'
)

@discover_pb.route('/', methods=['GET'])
def discover_all():
    result = db.session.execute('select * from venue')
    venues = result.fetchall()
    return render_template(
        'discover_all.jinja2',
        venues=venues
    )

@discover_pb.route("/search", methods=['GET', 'POST'])
def discover_query():
    query = request.args["query"]
    query_cleaned = query.lower()
    sql =   ("select * from scoop.venue "
            + "where lower(street_address) like :query_cleaned "
            + "or postal_code like :query_cleaned "
            + "or lower(city) like :query_cleaned " 
            + "or lower(neighbourhood) like :query_cleaned"
            )
    result = db.session.execute(sql, {"query_cleaned":"%"+query_cleaned+"%"})
    venues = result.fetchall()
    return render_template(
        "discover_results.jinja2", 
        venues=venues,
        query=query
    )