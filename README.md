# SiriusSchedule
Create events in Google Calendar form Sirius schedule

## Step 1: Turn on the Google Calendar API

- Use this wizard to create or select a project in the Google Developers Console and automatically turn on the API.
- Click Continue, then Go to credentials.
- On the Add credentials to your project page, click the Cancel button.
- At the top of the page, select the OAuth consent screen tab. Select an Email address, enter a Product name if not already set, and click the Save button.
- Select the Credentials tab, click the Create credentials button and select OAuth client ID.
- Select the application type Other, enter the name "Google Calendar API Quickstart", and click the Create button.
- Click OK to dismiss the resulting dialog.
- Click the file_download (Download JSON) button to the right of the client ID.
- Move this file to your working directory and rename it `client_secret.json`

## Step 2: Settings

- Your team number -- `team_id`
- Turn On/Off reminders -- `reminders`
- Remiders time (minutes) -- `reminders_time`
- Reminders type: **popup** or **email** -- `reminders_type`

### You must do this every day
