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
    # recaptcha = RecaptchaField() todo: do later
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

class ReviewForm(FlaskForm):
    review = StringField(
        'Review',
        validators=[
            DataRequired()
        ]
    )
    ratearea = RadioField(
        'Rating', 
        choices=[
            ('5', '1 star.'), # id = rate-area-5 , value = 5
            ('4', '2 stars'), # id = rate-area-4, value = 4
            ('3', '3 stars'), # id = rate-area-3, value = 3
            ('2', '4 stars'),
            ('1', '5 stars')
        ],
        validators=[
            DataRequired()
        ])
    submit = SubmitField('Add a Review')

