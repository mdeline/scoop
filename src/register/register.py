from flask import Blueprint, render_template

register_pb = Blueprint(
    'register_pb', __name__,
    template_folder='templates',
    static_folder='static'
)

@register_pb.route("/register", methods=["GET"])
def register():
    return render_template(
        "register.jinja2",
        template="register-template"
    )