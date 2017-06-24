#dailysmsweather.py

import yweather
import sys
from twilio.rest import TwilioRestClient
from datetime import datetime
import time



def timeseconds(_now, hrs, mins):
  future = datetime(_now.year, _now.month, _now.day, hrs, mins)
  if future > _now:
    _sleeptime = future - _now
  else:
    future = datetime(_now.year, _now.month, _now.day+1, hrs, mins)
    _sleeptime = future - _now
  print(_sleeptime)
  print('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
  return int(_sleeptime.total_seconds())

def main():
  hours = 8
  mins = 0
  while True:
    now = datetime.now()
    sleeptime = timeseconds(now, hours, mins)

   #print(sleeptime)


#if now.hour==10 and now.minute==15:
    f = open('twilioAuth.txt', 'r')
    account_sid = f.readline().replace('\n', '')
    auth_token = f.readline().replace('\n', '')

    client = yweather.Client( )
    woeid = client.fetch_woeid("Fullerton, CA")
    weather = client.fetch_weather(woeid, metric=False)

    location = '{}, {}'.format(weather['location']['city'], weather['location']['region'])

    todaysForecast = weather['forecast'][0]

    forecastString = 'This is Todays Forecast: \n{} {} high: {} F low: {} F  {}'.format(location, todaysForecast['date'], todaysForecast['high'], todaysForecast['low'], todaysForecast['text']) 

    ACCOUNT_SID = str(account_sid)
    AUTH_TOKEN = str(auth_token)

    
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    recipient = '+17145147319'

    time.sleep(sleeptime)
    print('message sent...')
    client.messages.create( to_= recipient, from_="+16572209643",  body = forecastString )
    print('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
    time.sleep(30)  
  
if __name__=="__main__":
  main()