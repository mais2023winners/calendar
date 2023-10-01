from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']


def contactsFetch():
    """Shows basic usage of the People API.
    Prints the name of the first 10 connections.
    """
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
 
    contacts = []
    try:
        service = build('people', 'v1', credentials=creds)

        # Call the People API
        results = service.people().connections().list(
            resourceName='people/me',
            pageSize=10,
            personFields='names,emailAddresses').execute()
        connections = results.get('connections', [])

        for person in connections:
            display_name = person['names'][0]['displayName']
            email_addresses = [email['value'] for email in person['emailAddresses']]
            contacts.append({display_name: email_addresses[0]})
        return contacts
    except HttpError as err:
        print(err)


# if __name__ == '__main__':
#     main()

