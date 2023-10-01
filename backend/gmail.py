from __future__ import print_function
import base64
import os.path
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ["https://mail.google.com/"]


def create_message(data):
    to_emails = ", ".join(data["to"])
    message = MIMEText(data["body"])
    message["to"] = to_emails
    message["from"] = "me"
    message["subject"] = data["subject"]
    return {"raw": base64.urlsafe_b64encode(message.as_bytes()).decode()}


def send_message(message, userToken):
    creds = Credentials.from_authorized_user_info(userToken, SCOPES)
    service = build("gmail", "v1", credentials=creds)

    try:
        message = service.users().messages().send(userId="me", body=message).execute()
        print("Message Id: %s" % message["id"])
        return message
    except Exception as error:
        print(error)
