import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
service = build('calendar', 'v3', credentials=creds)


def createEvent(e,userToken):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = Credentials.from_authorized_user_info(userToken,SCOPES)
    service = build('calendar', 'v3', credentials=creds)
    try:

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        event = {
            'summary': e['summary'],
            'location': e.get("location", None),
            'description': e.get("description", None),
            'start': {
                'dateTime': e['startDate'],
                'timeZone': 'America/Montreal',
            },
            'end': {
                'dateTime': e['endDate'],
                'timeZone': 'America/Montreal',
            },
            'attendees': e.get("attendeesEmailAddresses", []),
        }
        event = service.events().insert(calendarId='primary', body=event).execute()
        return f'Event created: {event.get("htmlLink")}'
    except HttpError as error:
        print('An error occurred: %s' % error)


tester = {
    "startDate": "2023-09-30T17:00:00-07:00",
    "endDate": "2023-09-30T18:00:00-07:00",
    # // name of the event
    "summary": "Cool Event for Cool Kids",
    "description": "this is a very cool event pls come",
    "attendeesEmailAddresses": [],
    "location": "mcgill trottier building"
}
if __name__ == '__main__':
    createEvent(tester)


def calendarFetch():
    page_token = None
    while True:
        events = service.events().list(calendarId='primary', pageToken=page_token).execute()
        for event in events['items']:
            event_data = [event['start'], event['end']]
            if 'location' in event:
                event_data.append(event['location'])
            if 'summary' in events:
                event_data.append(event['summary'])
            if 'description' in event:
                event_data.append(event['description'])
        page_token = events.get('nextPageToken')
        if not page_token:
            break

    return event_data
