from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    userName = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
