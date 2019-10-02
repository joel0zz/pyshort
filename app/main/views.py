from flask import request

from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    return 'hello world'