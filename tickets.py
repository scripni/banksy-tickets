import urllib2
import time
from twilio.rest import TwilioRestClient 
 
# replaced at runtime
ACCOUNT_SID = "--redacted--" 
AUTH_TOKEN = "--redacted--" 

# who are you gonna call?
phones = ['+353122122211', '+353122122211']

while True:
  try:
    request = urllib2.urlopen("http://dismaland.seetickets.com/tour/dismaland/list/1/100")
    body = request.read()
    # ticket html elements have a datetime attribute, check for the day we're there
    if 'datetime="2015-09-18"' in body:
      print "found"
      
      # text everyone
      client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)  
      for phone in phones:
        client.messages.create( 
          from_="banksy",
          to=phone,
          body="http://dismaland.seetickets.com/tour/dismaland/list/1/100"
        )

      print "sent messages"
      break
    else:
      print "not found, waiting 1 min"
      time.sleep(60)
  except Exception as ex:
    print ex
  else:
    request.close()
