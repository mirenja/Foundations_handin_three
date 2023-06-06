import os
from google.oauth2 import service_account
from googleapiclient.discovery import build


SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# scope is the application only needs read-only access to Gmail.

def get_gmail_service():
    credentials = service_account.Credentials.from_service_account_file(
        './client_secret.json', scopes=SCOPES)
    return build('gmail', 'v1', credentials=credentials)

# The service_account module allows you to authenticate using a service account, which is a type of Google account that represents non-human entities 
#  The build function is used to create a service object that can interact with the Gmail API.

