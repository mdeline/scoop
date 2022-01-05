from flask import Blueprint, render_template

login_pb = Blueprint(
    'login_pb', __name__,
    template_folder='templates',
    static_folder='static'
)

@login_pb.route("/login", methods=["GET"])
def login():
    return render_template(
        "login.jinja2",
        template="login-template"
    )