import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']


def get_gmail_service():

    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("gmail", "v1", credentials=creds)

    return service


def read_emails():

    service = get_gmail_service()

    results = service.users().messages().list(
        userId='me',
        maxResults=5
    ).execute()

    messages = results.get("messages", [])

    emails = []

    for msg in messages:

        txt = service.users().messages().get(
            userId='me',
            id=msg['id']
        ).execute()

        snippet = txt["snippet"]

        emails.append({
            "id": msg["id"],
            "subject": snippet
        })

    return emails


def move_to_spam(message_id):

    service = get_gmail_service()

    service.users().messages().modify(
        userId='me',
        id=message_id,
        body={
            "addLabelIds": ["SPAM"]
        }
    ).execute()

    print("Email moved to SPAM folder")