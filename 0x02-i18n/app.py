#!/usr/bin/env python3
'''
Config Class
'''

from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
from typing import Union
import pytz

app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    # Locale from URL parameter
    locale: str = request.args.get('locale', '')
    if locale in app.config['LANGUAGES']:
        return locale

    # Locale from user settings
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # Locale from request header
    req: str = request.headers.get('locale', '')
    if req in app.config['LANGUAGES']:
        return req

    # Default locale
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone():
    '''
    Get the timezone
    '''
    # Find timezone from URL parameters
    timezone: str = request.args.get('timezone', '')
    if not timezone and g.user:
        # Find timezone from user settings
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        pass

    # Default to UTC
    return app.config['BABEL_DEFAULT_TIMEZONE']


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
    Returns the index.html from the templates
    directory
    '''
    g.time = format_datetime()
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
