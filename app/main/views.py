from flask import request, render_template

from . import main
from .forms import UrlForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = UrlForm()
    return render_template('main/index.html', form=form)
