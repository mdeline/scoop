from flask import Blueprint, render_template, redirect, url_for, session
from werkzeug.security import check_password_hash, generate_password_hash
from os import getenv
from ..forms import RegisterForm, LoginForm # Needed to add this import to __init__.py first
from .. import db

auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hash_value = generate_password_hash(form.password.data)
        sql = "INSERT INTO scoop.user (name, email, password) VALUES (:name, :email, :password)"
        db.session.execute(sql, {"name":form.name.data, "email":form.email.data, "password":hash_value})
        db.session.commit()
        return redirect(url_for("auth_bp.success"))
    return render_template(
        "register.jinja2",
        form=form,
        template="register-template"
    )

@auth_bp.route('/success', methods=['GET', 'POST'])
def success():
    return render_template(
        "success.jinja2",
        template="success-template"
    )

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    failed_login = ''
    if form.validate_on_submit():
        sql = 'select * from scoop.user where email = :email'
        user = db.session.execute(sql, {'email': form.email.data}).first()
        hashed_password = user.password
        if user and check_password_hash(hashed_password, form.password.data):
            session["name"] = user.name
            return redirect(url_for("auth_bp.success"))
        failed_login = 'Invalid email or password.'
    return render_template(
        'login.jinja2',
        form=form,
        title='Log in.',
        template='login-page',
        failed_login = failed_login
    )

@auth_bp.route("/logout")
def logout():
    del session["name"]
    return redirect(url_for("home_bp.home"))
