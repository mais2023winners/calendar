import datetime
import os.path
from json import dumps
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
import uuid
import datetime


# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]

# if os.path.exists('token.json'):
#   creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# service = build('calendar', 'v3', credentials=creds)


def createEvent(e, userToken):
    print(userToken)
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """

    # save userTo to {uuid}.json
    # creds = None
    creds = Credentials.from_authorized_user_info(userToken, SCOPES)
    service = build("calendar", "v3", credentials=creds)

    attendees = []
    if "attendeesEmailAddresses" in e:
        for email in e["attendeesEmailAddresses"]:
            attendees.append({"email": email})

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
            "attendees": attendees,
        }
        event = service.events().insert(calendarId="primary", body=event).execute()
        eventLink = event.get("htmlLink")
        return eventLink
    except HttpError as error:
        print("An error occurred: %s" % error)


def calendarFetch(userToken):
    page_token = None
    while True:
        creds = Credentials.from_authorized_user_info(userToken, SCOPES)
        service = build("calendar", "v3", credentials=creds)

        timeMin = datetime.datetime.utcnow() - datetime.timedelta(days=7)
        timeMin = timeMin.isoformat() + "Z"
        timeMax = datetime.datetime.utcnow() + datetime.timedelta(days=7)
        timeMax = timeMax.isoformat() + "Z"
        events = (
            service.events()
            .list(
                calendarId="primary",
                pageToken=page_token,
                timeMin=timeMin,
                timeMax=timeMax,
            )
            .execute()
        )
        finalEvents = []
        for event in events["items"]:
            print(event)
            if event.get("start") is None:
                continue
            event_data = {
                "start": event["start"],
                "end": event["end"],
            }
            if "location" in event:
                # event_data.append(event["location"])
                event_data["location"] = event["location"]

            if "summary" in events:
                # event_data.append(event["summary"])
                event_data["summary"] = event["summary"]
            if "description" in event:
                # event_data.append(event["description"])
                event_data["description"] = event["description"]
            finalEvents.append(event_data)

        page_token = events.get("nextPageToken")
        if not page_token:
            break

    return finalEvents[0:100]


if __name__ == "__main__":
    createEvent(
        {
            "startDate": "2022-03-01T20:00:00.000Z",
            "endDate": "2022-03-01T22:00:00.000Z",
            "summary": "New Event",
        },
        {
            "access_token": "ya29.a0AfB_byC_Agn23bFWIy9UAYu1JUoDP5oEGrVrQ8GUE9U5yo0LhNBjmBLNAVfWgH0Yu3SI6Rhp2cJ0ja0HTDqFFJjnx331O8BQJGrpoqwjqzSPlqozCdOQ6ohrx8VUQB6vv01ai3Y7ktlBsNE5evdBC7C_G3k3AJS6I0f9aCgYKAS4SARMSFQGOcNnCAr1Up2OOgYX2shorFqnmkw0171",
            "expires_in": 3599,
            "refresh_token": "1//0dujYTmsTO4o1CgYIARAAGA0SNwF-L9IrCq-nvJ5ykQCqzvp3aqfo_fC40rsCEYJ6V7xN5Lm5-JgLbaPZoF_Nt51Qbn9l0cb-aoM",
            "scope": "https://www.googleapis.com/auth/gmail.modify https://www.googleapis.com/auth/calendar openid https://mail.google.com/ https://www.googleapis.com/auth/calendar.events https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile",
            "token_type": "Bearer",
            "id_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6ImI5YWM2MDFkMTMxZmQ0ZmZkNTU2ZmYwMzJhYWIxODg4ODBjZGUzYjkiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI3NDk2MzY0NjEyMi1pajFwaXBtb2wzMGNmc3B2cjBxMXY5cmI0MHF1ZGUydi5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsImF1ZCI6Ijc0OTYzNjQ2MTIyLWlqMXBpcG1vbDMwY2ZzcHZyMHExdjlyYjQwcXVkZTJ2LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTAxMTU0NzAxMzkwMzAzMzcwODgzIiwiZW1haWwiOiJtYWlzaGFja3NhY2NAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImF0X2hhc2giOiJ6RzJnN1o1Q3ZoV0NBdGYxbnl2Zm53IiwibmFtZSI6Ik1BSVMgSEFDS1MiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jTFhRbS1lQ2swZ0ZxUnJwOHhTRm9GMkd4UU1QV3IyRTlrY2FaZDNacVJKPXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6Ik1BSVMiLCJmYW1pbHlfbmFtZSI6IkhBQ0tTIiwibG9jYWxlIjoiZW4iLCJpYXQiOjE2OTYwMjgzMjQsImV4cCI6MTY5NjAzMTkyNH0.NMa6CRQ9ncrONvtdzjJSUY1Z9um4Y8e8vI-fN_R1fcxfeasy6zWjj9J2ZWVWhqsM23k5dD6HVHAm7aiDwss9u3SXusuY8bAqcbScCJ_UUbSxO39YEMNJN35c4Rg2i0-FRMb2Gb1SIHouoGWlfzNJY6c93Bxx3-KGgOPqgKJs-Oyu6BWmzT2d5eTgOqTAB74dMW3GqvwIn2WcVgzZ3QmnlcoWR7sgK7oM9MkOyR-a9IQu5FDJF7qeRsn01LOjV5UuvtUpp2xysFUBQtExqfe3MGOO9AZtax_p3D5Fn6iCjhk50d1eZ7NKSEkyDAJTcSEGPMf3usBLlL3KOu40SHFPTQ",
        },
    )
