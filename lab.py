import requests
import logging
from pprint import pprint
import os
from datetime import datetime

# change city_name variable for different cities
city_name = 'minneapolis,mn,us'
api_key = os.environ.get('WEATHER_KEY')

url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&units=imperial&appid={api_key}'
logging.basicConfig(format='%(asctime)s %(message)s', filename='debug.log', filemode='w', level=logging.WARNING)

try:
    data = requests.get(url).json()

    city_name = data['city']['name']
    interval_list = data['list']

    for periodic_report in interval_list:
        # datetime formatting will display in user's time to avoid confusion

        time_stamp = periodic_report['dt']
        date_time = datetime.fromtimestamp(time_stamp)
        date = date_time.strftime("%x")
        hour = date_time.strftime("%I")
        am_pm = date_time.strftime("%p")

        temp = periodic_report['main']['temp']
        wind_speed = periodic_report['wind']['speed']
        print(f'Date and time: {date}, {hour} {am_pm}\n'
              f'the temperature will be: {temp}\n'
              f'the wind speed will be: {wind_speed}\n')
except ValueError:
    print('Some incorrect information has been provided, error')
    logging.exception('Value error')
except Exception as e:
    print('An error has occurred')
    logging.exception(f'unexpected Exception has been raised')
