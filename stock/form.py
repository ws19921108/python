#-*-coding:utf-8-*-

from flask_wtf  import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    login = SubmitField('Login')