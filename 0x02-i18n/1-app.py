#!/usr/bin/env python3
'''
Config Class
'''

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    '''
    Config Class: Used along side with the 'app.config.from.object()
    function provided by babel to config it'
    '''
    LANGUAGES: list = ['en', 'fr']
    BABEL_DEFAULT_LOCALE: str = 'en'
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    '''
    Returns the 1-index.html from the templates
    directory
    '''
    return render_template('/1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
