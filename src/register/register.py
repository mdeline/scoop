from flask import Blueprint, render_template
from ..forms import RegisterForm # Needed to add this import to __init__.py first

register_pb = Blueprint(
    'register_pb', __name__,
    template_folder='templates',
    static_folder='static'
)

@register_pb.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegisterForm()
    return render_template(
        "register.jinja2",
        form=register_form,
        template="register-template"
    )