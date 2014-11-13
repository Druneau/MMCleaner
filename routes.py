"""
Routes and views for the bottle application.
"""

from bottle import route, view, response
from datetime import datetime

#meteo.py contains code to get weather information
from meteo import getLongForecast, getShortForecast

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