#!/usr/bin/env python3
'''
Config Class
'''

from flask import Flask, render_template, request
from flask_babel import Babel, _

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


@babel.localeselector
def get_locale() -> str:
    '''
    Selects a langauage translation to use for the request
    '''
    lang = request.accept_languages.best_match(app.config['LANGUAGES'])
    return lang or app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index() -> str:
    '''
    Returns the 3-index.html from the templates
    directory
    '''
    home_title, home_header = 'Welcome to Holberton', 'Hello world'
    return render_template('/3-index.html', home_title=home_title, home_header=home_header)  # noqa


if __name__ == "__main__":
    app.run(debug=True)
