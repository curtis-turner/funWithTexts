#simpleweatherreport.py

import yweather
import sys

client = yweather.Client( )
woeid = client.fetch_woeid("Fullerton, CA")
weather = client.fetch_weather(woeid, metric=False)

#for k in iter(weather):
 #print('key is{}:'.format(k))
 #print('\t{}'.format([k]))
 #print (k)

#print(weather[k])

location = '{}, {}'.format(weather['location']['city'], weather['location']['region'])

#print(location)

#for day in weather['forecast']:
  #print(day)

todaysForecast = weather['forecast'][0]

forecastString = 'This is Todays Forecast: \n {} {} high: {} F low: {} F  {}'.format(location, todaysForecast['date'], todaysForecast['high'], todaysForecast['low'], todaysForecast['text']) 

print(forecastString)