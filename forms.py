from flask_wtf import FlaskForm
from wtforms import validators, StringField


class OurForm(FlaskForm):
    name = StringField('Name:', validators=[validators.required()])

