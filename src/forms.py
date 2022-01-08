from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    DateField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField
)
from wtforms.validators import URL, DataRequired, Email, EqualTo, Length

class RegisterForm(FlaskForm):
    name = StringField(
        'Name',
        [DataRequired()]
    )
    email = StringField(
        'Email',
        [Email(message=('Email format is invalid.')), DataRequired()]
    )
    password = PasswordField(
        "Password",
        [DataRequired(message="Please enter a password.")],
    )
    confirmPassword = PasswordField(
        "Repeat Password",
        [EqualTo("password", message="Passwords must match.")]
    )

    # recaptcha = RecaptchaField() todo: do later
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message='Email format is invalid.')
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired()
        ]
    )
    submit = SubmitField('Log In')