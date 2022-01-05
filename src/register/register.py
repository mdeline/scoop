from flask import Blueprint, render_template, redirect, url_for
from ..forms import RegisterForm # Needed to add this import to __init__.py first

register_pb = Blueprint(
    'register_pb', __name__,
    template_folder='templates',
    static_folder='static'
)

success_pb = Blueprint(
    'success_pb', __name__,
    template_folder='templates',
    static_folder='static'
)

@register_pb.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        return redirect(url_for("register.success")) # todo: fix bug
    return render_template(
        "register.jinja2",
        form=register_form,
        template="register-template"
    )

@success_pb.route("/success", methods=["GET", "POST"])
def success():
    return render_template(
        "success.jinja2",
        template="success-template"
    )