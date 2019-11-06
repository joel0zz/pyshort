from flask import request, render_template, flash, redirect, url_for
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
            url = Url(url=form.url.data.strip("/"), short_url=random_string())
            db.session.add(url)
            db.session.commit()
            shortened_url = url_for('.short_url', short_id=url.short_url, _external=True)
            flash(f'Here is your shortened url: {shortened_url}', 'success')
            return redirect(url_for('main.index'))
        shortened_url = url_for('.short_url', short_id=url.short_url, _external=True)
        flash(f'Here is your shortened url: {shortened_url}', 'success')
    return render_template('main/index.html', form=form)


@main.route('/<short_id>', methods=['GET', 'POST'])
def short_url(short_id):
    url = Url.query.filter_by(short_url=short_id).first()
    return redirect(url.url)


def random_string(string_length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))
