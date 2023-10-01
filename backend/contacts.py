from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/contacts.readonly"]


def contactFetch(userToken):
    """Shows basic usage of the People API.
    Prints the name of the first 10 connections.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    try:
        creds = Credentials.from_authorized_user_info(userToken, SCOPES)
        service = build("people", "v1", credentials=creds)

        results = (
            service.people()
            .connections()
            .list(
                resourceName="people/me",
                pageSize=10,
                personFields="names,emailAddresses",
            )
            .execute()
        )
        connections = results.get("connections", [])
        contacts = []
        for person in connections:
            if person.get("emailAddresses") is None:
                continue
            display_name = person["names"][0]["displayName"]
            email_addresses = [email["value"] for email in person["emailAddresses"]]
            contacts.append({display_name: email_addresses[0]})
        return contacts
    except HttpError as err:
        print(err)


# if __name__ == '__main__':
#     main()
