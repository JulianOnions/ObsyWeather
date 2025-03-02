
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import csv


# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1tF7B2aTjOWwbTBv-lQHReBWVYNwjWmkwjOqr1jJhWa4"
SAMPLE_RANGE_NAME = "Data!A2:C"

def getService():
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())
  return build("sheets", "v4", credentials=creds)


def checkData(data):
  try:
    float(data)
    return 'numberValue'
  except ValueError:
    pass
  return 'stringValue'
    

def loadValues(file):
  with open(file, newline="") as csvfile:
    reader = csv.reader(csvfile)
    return [{"values": [{"userEnteredValue": {checkData(f.strip()): f.strip()}} for f in e]} for e in reader]
    # return list(reader)

def main():
  try:
    service = getService()
    print("Service:", service)
    # appendValues(service)
    # Call the Sheets API
    sheet = service.spreadsheets()
    
    body = loadValues("WindyShort.txt")
    # print ("Body:", body); exit(0)
    result = sheet.values().append(
            spreadsheetId=SAMPLE_SPREADSHEET_ID,
            range=SAMPLE_RANGE_NAME,
            valueInputOption="RAW",
            body=body,
        ).execute()
  
      
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
  except HttpError as err:
    print(err)


if __name__ == "__main__":
  main()
# [END sheets_quickstart]
