import datetime
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json
SCOPES = ["https://www.googleapis.com/auth/calendar"]

def createEvent(e, userToken):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """

    creds = Credentials.from_authorized_user_info(
        userToken, SCOPES)
    service = build('calendar', 'v3', credentials=creds)
    
    try:
        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
        event = {
            "summary": e["summary"],
            "location": e.get("location", None),
            "description": e.get("description", None),
            "start": {
                "dateTime": e["startDate"],
                "timeZone": "America/Montreal",
            },
            "end": {
                "dateTime": e["endDate"],
                "timeZone": "America/Montreal",
            },
            "attendees": e.get("attendeesEmailAddresses", []),
        }
        event = service.events().insert(calendarId="primary", body=event).execute()
        return f'Event created: {event.get("htmlLink")}'
    except HttpError as error:
        print('An error occurred: %s' % error)


def calendarFetch(userToken):
    creds = Credentials.from_authorized_user_info(userToken, SCOPES)
    service = build("calendar", "v3", credentials=creds)
    page_token = None
    while True:
        events = service.events().list(calendarId='primary', pageToken=page_token).execute()
        event_data = []
        for event in events['items'][-100:]:
            event_data.append({'start': event['start']})
            event_data.append({'end': event['end']})
            if 'location' in event:
                event_data.append({'location': event['location']})
            if 'summary' in event:
                event_data.append({'title': event['summary']})
            if 'description' in event:
                event_data.append({'description': event['description']})
        page_token = events.get('nextPageToken')
        if not page_token:
            break
    return event_data
