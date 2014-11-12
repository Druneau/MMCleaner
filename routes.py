"""
Routes and views for the bottle application.
"""

from bottle import route, view, response
from datetime import datetime

#meteo.py contains code to get weather information
from meteo import getLongForecast, getShortForecast

@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/')
@route('/<station>')
@view('meteo')
def meteo(station='caqc0177'):
    """Renders the meteo page."""
    long=getLongForecast(station)
    return dict(
        title= long[0] + " - " + station,
        message=datetime.now(),
        year=datetime.now().year,
        longTerm=long[1],
        shortTerm=getShortForecast(station)
    )
