#!/usr/bin/env python3
'''
Config Class
'''

from flask import Flask, render_template, request, g
from flask_babel import Babel

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
    locale = request.args.get('locale')
    if locale in ['en', 'fr']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> dict:
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
    username = None
    if (g.user):
        username: str = g.user.get('name')
    return render_template('5-index.html', username=username)


if __name__ == "__main__":
    app.run(debug=True)
