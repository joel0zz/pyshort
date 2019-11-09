from flask import render_template, flash, redirect, url_for
import random
import string

from . import main
from .forms import UrlForm
from .. import db
from ..models import Url


@main.route('/', methods=['GET', 'POST'])
def index():
    form = UrlForm()
    if form.validate_on_submit():
        url = Url.query.filter_by(url=form.url.data).first()
        if url is None:
            url = Url(url=form.url.data.strip("/"), short_url=_random_string())
            db.session.add(url)
            db.session.commit()
            flash(f'Here is your shortened url: {_url_generator(url)}', 'success')
            return redirect(url_for('main.index'))
        flash(f'Here is your shortened url: {_url_generator(url)}', 'success')
    return render_template('main/index.html', form=form)


@main.route('/<short_id>', methods=['GET', 'POST'])
def short_url(short_id):
    try:
        url = Url.query.filter_by(short_url=short_id).first()
        return redirect(url.url)
    except AttributeError:  # handle when index is loaded without <short_id> e.g first page load.
        pass


def _random_string(string_length=10):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(string_length))


def _url_generator(url):
    return url_for('.short_url', short_id=url.short_url, _external=True)
