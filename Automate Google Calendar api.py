# Import the necessary libraries
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up the necessary credentials and authorization
creds, _ = google.auth.default()
service = build('calendar', 'v3', credentials=creds)

# Define the event details
event = {
  'summary': 'Test Event',
  'location': '123 Main Street',
  'description': 'This is a test event.',
  'start': {
    'dateTime': '2022-01-01T09:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
 
 },
  'end': {
    'dateTime': '2022-01-01T17:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'attendees': [
    {'email': 'attendee1@example.com'},
    {'email': 'attendee2@example.com'},
  ],
  'reminders': {
    'useDefault': True
  },
}

# Create the event
event = service.events().insert(calendarId='primary', body=event).execute()
print(f'Event created: {event.get("htmlLink")}')
