from flask import flash, Blueprint, render_template, request, redirect, url_for, session
from .. import db

venue_bp = Blueprint(
    "venue_bp", __name__,
    template_folder="templates",
    static_folder="static"
)

@venue_bp.route("/<venue_id>", methods=["GET"])
def venue(venue_id):
    # Last venue page visited
    session["recent_venue"] = venue_id

    # Venue info
    venue = db.session.execute(
        "select * from scoop.venue where id = :venue_id",
        {"venue_id": venue_id}
    ).fetchone()

    # Review count & review average
    review_aggregates = db.session.execute("""
        select 
            coalesce(avg(stars)::numeric(3,2), 0) as review_avg,
            coalesce(count(review), 0) as review_count
        from scoop.review
        where venue_id = :venue_id
        and deleted = false;
        """,
        {"venue_id": venue_id}
    ).fetchone()

    # Reviews
    reviews = db.session.execute("""
        select 
            review.id, 
            review, 
            stars, 
            appuser.fullname as user,
            appuser_id, 
            created_at, 
            modified_at, 
            img_url as user_photo 
        from scoop.review
        inner join scoop.appuser on scoop.appuser.id = scoop.review.appuser_id
        where venue_id = :venue_id
        and deleted = false
        order by created_at desc
    """,
    {"venue_id":venue_id}
    ).fetchall()

    if venue:
        return render_template(
            "venue.jinja2",
            venue=venue,
            review_aggregates=review_aggregates,
            reviews=reviews
        )
    else:
        return redirect(url_for("home_bp.home"))
        
@venue_bp.route("/review", methods=["POST"])
def review():
    review = request.form.get("review")
    rating = request.form.get("rating")
    venue_id = request.form.get("venue_id")
    appuser_id = session.get("appuser_id")

    if review and rating and appuser_id:
        sql = """
            insert into scoop.review(review, stars, appuser_id, venue_id, deleted) 
            values(:review, :rating, :appuser_id, :venue_id, false);
        """
        db.session.execute(sql, {
            "review": review,
            "rating": rating,
            "appuser_id": appuser_id,
            "venue_id": venue_id,  
        })
        db.session.commit()
    else:
        flash("Please fill both review and rating fields.")
    return redirect(url_for("venue_bp.venue", venue_id=venue_id))

@venue_bp.route("/<venue_id>/review/<review_id>", methods=["GET"])
def get_review(venue_id, review_id):
    review = db.session.execute(
        "select * from scoop.review where id = :review_id",
        {"review_id": review_id}
    ).fetchone()

    if review and session.get("appuser_id") == review.appuser_id:
        return render_template(
            "edit_review.jinja2",
            review=review
        )
    return redirect(url_for("home_bp.error")) 

@venue_bp.route("/<venue_id>/review/<review_id>", methods=["GET", "POST"])
def edit_review(venue_id, review_id):
    review = request.form.get("review")
    rating = request.form.get("rating")

    # Review"s writer
    review_writer = db.session.execute(
        "select appuser_id from scoop.review where id = :review_id",
        {"review_id": review_id}
    ).fetchone().appuser_id

    if review and rating and session.get("appuser_id") == review_writer:
        db.session.execute(
            "update scoop.review set review = :review, stars = :stars, modified_at = now() "
            + "where id = :review_id",
            {
                "review": review,
                "stars": rating,
                "review_id": review_id
            }
        )
        db.session.commit()
        return redirect(url_for("venue_bp.venue", venue_id=venue_id))
    else:
        flash("Please fill both review and rating fields.")
        return redirect(url_for("venue_bp.edit_review", review_id=review_id, venue_id=venue_id))

@venue_bp.route("/<venue_id>/review/<review_id>/delete", methods=["GET"])
def delete_review(venue_id, review_id):
    # Current user
    review_writer = db.session.execute(
        "select appuser_id from scoop.review where id = :review_id",
        {"review_id": review_id}
    ).fetchone().appuser_id

    if session["appuser_id"] and session["appuser_id"] == review_writer:
        db.session.execute(
            "update scoop.review set deleted = true "
            + "where id = :review_id",
            {"review_id": review_id}
        )
        db.session.commit()
    return redirect(url_for("venue_bp.venue", venue_id=venue_id))