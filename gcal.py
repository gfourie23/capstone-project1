from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
from datetime import date


SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
CAL = discovery.build('calendar', 'v3', http=creds.authorize(Http()))

CALENDAR_ID = '38548fc33eba6c5b2b0d424e6fa144084a3ccf33be3b4e3d92b9b51389d317de@group.calendar.google.com'

TIMEZONE = 'America/Denver'
event = {
  'summary': 'Michael Scott',
  'location': '800 Howard St., San Francisco, CA 94103',
  'description': 'A chance to hear more about Google\'s developer products.',
  'start': {
    'dateTime': '2023-12-06T07:00:00-08:00',
    'timeZone': TIMEZONE,
  },
  'end': {
    'dateTime': '2023-12-06T8:00:00-08:00',
    'timeZone': TIMEZONE,
  },
  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=2'
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}

event = CAL.events().insert(calendarId=CALENDAR_ID, body=event).execute()
print ('Event created: %s' % (event.get('htmlLink')))
    
    
    
    
    
    
"""'summary': 'Patient Francesca',
    'start': {'dateTime': '2023-12-06T9:00', 'timezone':TIMEZONE},
    'end': {'dateTime': '2023-12-06T10:00', 'timezone':TIMEZONE},
    'recurrence': {'RRULE:FREQ=WEEKLY;INTERVAL=2;UNTIL=20240131'}
}


CALENDAR_ID = '38548fc33eba6c5b2b0d424e6fa144084a3ccf33be3b4e3d92b9b51389d317de@group.calendar.google.com'

event = CAL.events().insert(calendarId='primary', sendNotifications=True, body=event).execute()

print('''
      ***%r event (ID: %s) modified:
      Start: %s
      End: %s
      
      ''' % (event['summary'].encode('utf-8'), event['id'], event['start']['dateTime'], event['end']['dateTime'], event['recurrence'][0]))"""
