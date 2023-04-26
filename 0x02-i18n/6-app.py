#!/usr/bin/env python3
'''
Config Class
'''

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union

app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "de", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    '''
    Config Class: Used along side with the 'app.config.from.object()
    function provided by babel to config it'
    '''
    LANGUAGES: list = ['en', 'fr', 'de']
    BABEL_DEFAULT_LOCALE: str = 'en'
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    '''
    Selects a langauage translation to use for the request
    '''
    # Locale from URL parameter
    locale: str = request.args.get('locale')
    if locale in ['en', 'fr', 'de']:
        return locale

    # Locale from user settings
    if g.user.get('locale', None):
        return g.user.get('locale')

    # Locale from request header
    req: str = request.accept_languages.best_match(app.config['LANGUAGES'])
    if req:
        return req

    # Default locale
    return app.config['BABEL_DEFAULT_LOCALE']


def get_user() -> Union[dict, None]:
    '''
    Gets user if from users dictionary (utils.py)
    '''
    user_id: int = int(request.args.get('login_as')) if request.args.get('login_as') else None  # noqa
    return users.get(user_id) if user_id in users else None


@app.before_request
def before_request() -> None:
    '''
    gets user id, and stores it in g.user
    it will be the first function to run
    '''
    g.user: dict = get_user() if get_user() else None


@app.route('/')
def index() -> str:
    '''
    Returns the 5-index.html from the templates
    directory
    '''
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run()
