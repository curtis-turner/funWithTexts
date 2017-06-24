#smsweather.py

import yweather
import sys
from twilio.rest import TwilioRestClient

f = open('twilioAuth.txt', 'r')
account_sid = f.readline().replace('\n', '')
auth_token = f.readline().replace('\n', '')

client = yweather.Client( )
woeid = client.fetch_woeid(sys.argv[1])
weather = client.fetch_weather(woeid, metric=False)

location = '{}, {}'.format(weather['location']['city'], weather['location']['region'])

todaysForecast = weather['forecast'][0]

forecastString = 'This is Todays Forecast: \n{} {} high: {} F low: {} F  {}'.format(location, todaysForecast['date'], todaysForecast['high'], todaysForecast['low'], todaysForecast['text']) 

ACCOUNT_SID = str(account_sid)
AUTH_TOKEN = str(auth_token)

    
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
recipient = str(sys.argv[2])

client.messages.create( to_= recipient, from_="+16572209643",  body = forecastString )