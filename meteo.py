"""
Routes and views for the bottle application.
"""

from datetime import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

def getLongForecast(station):
    page = urlopen('http://mobile.theweathernetwork.com/fivedayforecast/' + station)
    soup = BeautifulSoup(page)
    tables = soup.find_all("table")
    title = soup.find('p', {'class' : 'title'}).contents[0].string 
    table = tables[3]
    cleanText = table.get_text()
    cleanerText=cleanText.replace('\t', '\r').replace('\n', '\r').replace('\r',',')
    dirtyList = [x.strip() for x in cleanerText.split(',')]
    cleanList = [x for x in dirtyList if x]
    forcast = cleanList

    return [title, forcast]

def getShortForecast(station):
    page = urlopen('http://mobile.theweathernetwork.com/next24hours/' + station)
    soup = BeautifulSoup(page)
    tables = soup.find_all("table")
    table = tables[3]
    cleanText = table.get_text()
    cleanerText=cleanText.replace('\t', '\r').replace('\n', '\r').replace('\r',',')
    dirtyList = [x.strip() for x in cleanerText.split(',')]
    cleanList = [x for x in dirtyList if x]
    forcast = cleanList

    return forcast