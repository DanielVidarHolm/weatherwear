from requests import Request, Session
from requests.exceptions import TooManyRedirects, Timeout, ConnectionError
import json
import os

                     

# CORDINATES

def getWeatherData(cord):
    url = "http://api.openweathermap.org/data/2.5/forecast"
    parameters = {
        'appid': 'c94a7661f00720f210cd3bf33f02e5d7',
        'lat': cord[0],
        'lon': cord[1],
        'cnt': '4',
        'units': 'metric'
    }

    session = Session()
    try:
        r = session.get(url,params=parameters)
        data = json.loads(r.text)
        return data
    except (TooManyRedirects, Timeout, ConnectionError) as e:
        print(e)

# Implement this later when i make a gui app
# TODO
def getCordinates():
    pass
def sendMessage(message):
    url = "https://api.telegram.org/bot5186720358:AAGzPQ4M0tgKdTgkiHyz4ohMwd7hRDWdEUo/sendMessage"
    parameters = {
        'chat_id': "5163053321",
        'text': message
    }
    session = Session()
    try:
        session.get(url,params=parameters)
    except (TooManyRedirects, Timeout, ConnectionError) as e:
        print(e)






