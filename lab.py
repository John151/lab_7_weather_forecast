import requests
from pprint import pprint
import os
from datetime import datetime

city_name = 'minneapolis,mn,us'
api_key = os.environ.get('WEATHER_KEY')
print(api_key)
url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&units=imperial&appid={api_key}'

data = requests.get(url).json()
print('Whoopsie daisey')


city_name = data['city']['name']
interval_list = data['list']

for periodic_report in interval_list:
    # datetime formatting from datatime
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

#
# print(f'Weather forcast for\ncity name: {city_name}')
# temp = data['main']['temp']
#
# print(f'The current temperature is {temp}')
