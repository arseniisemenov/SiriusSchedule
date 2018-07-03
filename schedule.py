import json
import requests
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime

# Your team number
team_id = 24

# Reminders settings
reminders = True
reminders_time = 10 #minutes
reminders_type = 'popup' #popup or email

# Getting timetable
response = requests.get('https://scheduler.talantiuspeh.ru/app.php/meeting/display?name=%D0%9D%D0%B0%D1%83%D0%BA%D0%B0')
data = json.loads(response.text)
meetings = data[team_id-1]['meetings']

# Setup the Calendar API
SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))

# Creating events
for meeting in meetings:
    event = {
    'summary': meeting['title'],
    'start': {
        'dateTime': meeting['start'],
    },
    'end': {
        'dateTime': meeting['end'],
    },
    }
    if reminders:
        event['reminders'] = {
        'useDefault': False,
        'overrides': [
        {'method': reminders_type, 'minutes': reminders_time},
        ],
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))
    