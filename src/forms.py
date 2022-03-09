from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    DateField,
    PasswordField,
    SelectField,
    StringField,
    RadioField,
    SubmitField
)
from wtforms.validators import URL, DataRequired, Email, EqualTo, Length

class RegisterForm(FlaskForm):
    fullname = StringField(
        'Name',
        validators=[
            DataRequired()
        ]
    )
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message='Email format is invalid.')
        ]
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=5)
        ]
    )
    confirmPassword = PasswordField(
        "Repeat Password",
        validators=[
            EqualTo('password', message="Passwords must match."),  
        ]
    )
    submit = SubmitField('Submit')

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
    submit = SubmitField('Submit')
