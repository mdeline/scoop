from flask import Blueprint, render_template, redirect, url_for
from ..forms import RegisterForm # Needed to add this import to __init__.py first

# Blueprint Configuration
auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template(
        "login.jinja2",
        template="login-template"
    )

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        return redirect(url_for("auth_bp.success"))
    return render_template(
        "register.jinja2",
        form=register_form,
        template="register-template"
    )

@auth_bp.route('/success', methods=['GET', 'POST'])
def success():
    return render_template(
        "success.jinja2",
        template="success-template"
    )