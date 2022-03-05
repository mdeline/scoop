from flask import Blueprint, render_template, request, session
from .. import db

discover_pb = Blueprint(
    'discover_pb', __name__,
    template_folder='templates',
    static_folder='static'
)

@discover_pb.route('/', methods=['GET'])
def discover_all():
    sql = '''
        with neighbourhood_images as (
	        select 
		        neighbourhood_id, 
		        img_url, 
    	        row_number() over (
    		        partition by neighbourhood order by random()
    	        ) as row_num
            from scoop.venue 
	        where neighbourhood_id is not null
            and img_url is not null
        ),
        neighbourhood_venues as (
	        select 
		        neighbourhood_id, 
		        count(*) as venues_count
            from scoop.venue
            group by neighbourhood_id
        )
        select 
	        nh.name, 
	        images.img_url, 
	        venues.venues_count
            from neighbourhood_images images
            inner join neighbourhood_venues venues on venues.neighbourhood_id = images.neighbourhood_id
            inner join scoop.neighbourhood nh on nh.id = images.neighbourhood_id
            where images.row_num = 1
            order by venues.venues_count desc;
    '''
    neighbourhoods = db.session.execute(sql).fetchall()

    return render_template(
        'discover.jinja2',
        neighbourhoods=neighbourhoods
    )

@discover_pb.route("/search", methods=['GET', 'POST'])
def discover_query():
    query = request.args["query"]
    query_cleaned = query.lower()

    sql_results = '''
        select * from venue
        where lower(name) like :query_cleaned
        or lower(street_address) like :query_cleaned
        or postal_code like :query_cleaned
        or lower(city) like :query_cleaned 
        or lower(neighbourhood) like :query_cleaned;
    '''

    sql_aggregates = '''
        select count(*) as count from venue
        where lower(name) like :query_cleaned
        or lower(street_address) like :query_cleaned
        or postal_code like :query_cleaned
        or lower(city) like :query_cleaned 
        or lower(neighbourhood) like :query_cleaned;
    '''

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
        "select * from venue where neighbourhood=:query;", 
        {"query":query}
    ).fetchall()

    venue_aggregates = db.session.execute(
        "select count(*) as count from venue where neighbourhood=:query;",
        {"query":query}
    ).fetchone()

    return render_template(
        "discover_results.jinja2", 
        venues=venues,
        venue_aggregates=venue_aggregates,
        query=query
    )