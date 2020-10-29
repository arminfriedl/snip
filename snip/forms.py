from flask_wtf import FlaskForm

from wtforms import StringField
from wtforms import validators

from .urlvalidator import URLValidator

class SnipForm(FlaskForm):
    # The URL validator from wtforms is rather simple and only used as a first
    # line of defense here. The URL is later validated again by urlvalidator.py
    # in snipper.py which can lead to a UrlValidationError.
    url = StringField('url', validators=[validators.InputRequired(),
                                         URLValidator(message='Please enter a URL like "https://example.com/example"')])
