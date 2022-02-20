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
    failed_registration = ''
    if form.validate_on_submit():
        sql = "select exists(select 1 from scoop.appuser where email=:email) as email_exists"
        email_exists = db.session.execute(sql, {'email':form.email.data.lower()}).first().email_exists
        if email_exists is False:
            hash_value = generate_password_hash(form.password.data)
            sql = "insert into appuser (fullname, email, password, role_id) VALUES (:fullname, :email, :password, 1)"
            db.session.execute(sql, {"fullname":form.fullname.data, "email":form.email.data.lower(), "password":hash_value})
            db.session.commit()
            return redirect(url_for("auth_bp.success"))
        failed_registration = 'Email already exists.'
    return render_template(
        "register.jinja2",
        form=form,
        title="Register",
        template="register-template",
        failed_registration=failed_registration
    )

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    failed_login = ''
    if form.validate_on_submit():
        sql = 'select * from scoop.appuser where email = :email'
        appuser = db.session.execute(sql, {'email': form.email.data.lower()}).first()
        if appuser:
            hashed_password = appuser.password
            if check_password_hash(hashed_password, form.password.data):
                session["appuser_fullname"] = appuser.fullname
                session["appuser_id"] = appuser.id
                return redirect(url_for("auth_bp.success"))
        failed_login = 'Invalid email or password.'
    return render_template(
        'login.jinja2',
        form=form,
        title='Login.',
        template='login-template',
        failed_login = failed_login
    )

@auth_bp.route('/success', methods=['GET', 'POST'])
def success():
    return redirect(url_for("home_bp.home"))

@auth_bp.route("/logout")
def logout():
    del session["appuser_id"]
    del session["appuser_fullname"]
    return redirect(url_for("home_bp.home"))
