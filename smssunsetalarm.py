#smssunsetalarm.py

import yweather
import sys
from twilio.rest import TwilioRestClient
from datetime import datetime
import time

def timeseconds(_now, hrs, mins):
  future = datetime(_now.year, _now.month, _now.day, hrs+12, mins)
  print(future)
  print(_now)
  if future > _now:
    _sleeptime = future - _now
  else:
    future = datetime(_now.year, _now.month, _now.day+1, hrs, mins)
    _sleeptime = future - _now
  #print(_sleeptime)
  #print('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
  return int(_sleeptime.total_seconds()-(5*60))


def main():
  
  while True:
    f = open('twilioAuth.txt', 'r')
    account_sid = f.readline().replace('\n', '')
    auth_token = f.readline().replace('\n', '')

    ACCOUNT_SID = str(account_sid)
    AUTH_TOKEN = str(auth_token)
  
    client = yweather.Client( )
    woeid = client.fetch_woeid("Fullerton, CA")
    weather = client.fetch_weather(woeid, metric=False)

    location = '{}, {}'.format(weather['location']['city'], weather['location']['region'])

    todaysSunset = weather['astronomy']
    todaysSunestString = 'Sunset time for today: {} '.format(todaysSunset['sunset'])
    message = 'it is 5 minutes till sunset get inside before the zombies get you!!!'

    hours = int(todaysSunset['sunset'][0])
    mins = int(todaysSunset['sunset'][2:4])
    #print(hours, ':', mins)
    print(todaysSunestString)

    now = datetime.now()
    sleeptime = timeseconds(now, hours, mins)
    
    #print(sleeptime)

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    recipient = '+17145147319'

    time.sleep(sleeptime)
    print('message sent...')
    client.messages.create( to_= recipient, from_="+16572209643",  body = message )
    print('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
    time.sleep(30)  
  

if __name__=="__main__":
  main()