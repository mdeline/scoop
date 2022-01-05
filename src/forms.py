from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    DateField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import URL, DataRequired, Email, EqualTo, Length

class RegisterForm(FlaskForm):
    first_name = StringField(
        'First Name',
        [DataRequired()]
    )
    last_name = StringField(
        'Last Name',
        [DataRequired()]
    )
    email = StringField(
        'Email',
        [
            Email(message=('Email format is invalid.')),
            DataRequired()
        ]
    )
    password = PasswordField(
        "Password",
        [DataRequired(message="Please enter a password.")],
    )
    confirmPassword = PasswordField(
        "Repeat Password",
        [EqualTo(password, message="Passwords must match.")]
    )
    recaptcha = RecaptchaField()
    submit = SubmitField("Submit")