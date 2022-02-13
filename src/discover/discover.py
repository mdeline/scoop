from flask import Blueprint, render_template, request, session
from .. import db

discover_pb = Blueprint(
    'discover_pb', __name__,
    template_folder='templates',
    static_folder='static'
)

@discover_pb.route('/', methods=['GET'])
def discover_all():
    neighbourhoods = db.session.execute(
        'with neighbourhood_images as ('
        + 'select neighbourhood, img_url, '
        + 'row_number() over ('
        + 'partition by neighbourhood order by random() '
        + ') as row_num '
        + 'from venue where neighbourhood is not null '
        + 'and img_url is not null), '
        + 'neighbourhood_venues as ('
        + 'select neighbourhood, count(*) as venues_count '
        + 'from venue '
        + 'group by neighbourhood) '
        + 'select i.neighbourhood as name, i.img_url, v.venues_count '
        + 'from neighbourhood_images i '
        + 'inner join neighbourhood_venues v on v.neighbourhood = i.neighbourhood '
        + 'where i.row_num = 1 '
        + 'order by v.venues_count desc'
    ).fetchall()

    return render_template(
        'discover.jinja2',
        neighbourhoods=neighbourhoods
    )

@discover_pb.route("/search", methods=['GET', 'POST'])
def discover_query():
    query = request.args["query"]
    query_cleaned = query.lower()

    sql_results = (
        "select * from venue "
        + "where lower(street_address) like :query_cleaned "
        + "or postal_code like :query_cleaned "
        + "or lower(city) like :query_cleaned " 
        + "or lower(neighbourhood) like :query_cleaned"
    )

    sql_aggregates = (
        "select count(*) as count from venue "
        + "where lower(street_address) like :query_cleaned "
        + "or postal_code like :query_cleaned "
        + "or lower(city) like :query_cleaned " 
        + "or lower(neighbourhood) like :query_cleaned"
    )

    venues = db.session.execute(
        sql_results, 
        {"query_cleaned":"%"+query_cleaned+"%"}
    ).fetchall()

    venue_aggregates = db.session.execute(
        sql_aggregates,
        {"query_cleaned":"%"+query_cleaned+"%"}
    ).fetchone()

    return render_template(
        "discover_results.jinja2", 
        venues=venues,
        query=query,
        venue_aggregates=venue_aggregates
    )

@discover_pb.route("/neighbourhood", methods=['GET', 'POST'])
def discover_neighbourhood():
    query = request.args["query"]

    venues = db.session.execute(
        "select * from venue where neighbourhood=:query", 
        {"query":query}
    ).fetchall()

    venue_aggregates = db.session.execute(
        "select count(*) as count from venue where neighbourhood=:query",
        {"query":query}
    ).fetchone()

    return render_template(
        "discover_results.jinja2", 
        venues=venues,
        venue_aggregates=venue_aggregates,
        query=query
    )