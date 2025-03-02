import MyService
from googleapiclient.errors import HttpError
import sys

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1tF7B2aTjOWwbTBv-lQHReBWVYNwjWmkwjOqr1jJhWa4"
SAMPLE_RANGE_NAME = "Data!A2:C"

def main():
  try:
    service = MyService.getService()
    print("Service:", service)
    # appendValues(service)
    # Call the Sheets API
    sheet = service.spreadsheets()
    
    values = MyService.loadValuesBasic("Windy.txt")
    body = {"values": values}

    # print ("Body:", body); exit(0)
    result = sheet.values().append(
            spreadsheetId=SAMPLE_SPREADSHEET_ID,
            range=SAMPLE_RANGE_NAME,
            valueInputOption="USER_ENTERED",
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
