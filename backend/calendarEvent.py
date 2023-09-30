import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def createEvent(e):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    try:
        service = build('calendar', 'v3', credentials=creds)

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
        print("ehhello")
        return f'Event created: {event.get("htmlLink")}'
    except HttpError as error:
        print('An error occurred: %s' % error)

tester = {
    "startDate": "2023-10-5T09:00:00-07:00",
    "endDate": "2023-10-6T09:00:00-07:00",
    # // name of the event
    "summary": "THis is a tester summary",
    "description": None,
    "attendeesEmailAddresses": [],
    "location": None
}
if __name__ == '__main__':
    createEvent(tester)