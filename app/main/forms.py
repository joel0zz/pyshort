from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError
from wtforms.validators import DataRequired
from urllib.parse import urlparse


class UrlForm(FlaskForm):
    url = StringField("Please enter the url you would like to shorten", validators=[DataRequired()])

    def validate_url(self, url):
        parsed_url = urlparse(url.data)
        if not parsed_url.netloc or not parsed_url.scheme:
            raise ValidationError("Please enter a valid URL.")
