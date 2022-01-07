from flask import Blueprint, render_template

discover_pb = Blueprint(
    'discover_pb', __name__,
    template_folder='templates',
    static_folder='static'
)

@discover_pb.route("/discover", methods=["GET"])
def discover():
    return render_template(
        "discover.jinja2",
        template="discover-template"
    )