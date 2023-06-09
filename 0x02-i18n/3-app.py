#!/usr/bin/env python3
'''
Config Class
'''

from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale() -> str:
    '''
    Selects a langauage translation to use for the request
    '''
    test = 0
    if (test):
        return 'fr'
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    '''
    Returns the 3-index.html from the templates
    directory
    '''
    h_t, h_h = 'Welcome to Holberton', 'Hello world!'
    return render_template('3-index.html', home_title=h_t, home_header=h_h)


if __name__ == "__main__":
    app.run(debug=True)
