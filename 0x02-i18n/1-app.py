#!/usr/bin/env python3
'''
Config Class
'''

from flask import Flask
from flask_babel import Babel
from typing import List

app = Flask(__name__)


class Config:
    '''
    Config Class: Used along side with the 'app.config.from.object()
    function provided by babel to config it'
    '''
    LANGUAGES: List[str, str] = ['en', 'fr']
    BABEL_DEFAULT_LOCALE: str = 'en'
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'


app.config.from_object(Config)
babel = Babel(app)
