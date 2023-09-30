from __future__ import print_function
import base64
import os.path
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ['https://mail.google.com/']


creds = Credentials.from_authorized_user_file('token.json', SCOPES)

service = build('gmail', 'v1', credentials=creds)


def extract_content(data):
    email_data = data["data"]
    recipients = email_data["to"]
    subject = email_data["subject"]
    body = email_data["body"]


def create_message(data):
    to_emails = ", ".join(data['to'])
    message = MIMEText(data['body'])
    message['to'] = to_emails
    message['from'] = "me"
    message['subject'] = data['subject']
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}


def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                   .execute())
        print('Message Id: %s' % message['id'])
        return message
    except Exception as error:
        print(error)


json_data = {'to': ['reheanrehean@gmail.com', 'rehean.thillai@gmail.com', 'a.ghellach@gmail.com'], 'subject': '2 times?', 'body': 'dededed'}
message = create_message(json_data)
# print(json_data['body'])
print(send_message(service=service, user_id='me', message=message))
