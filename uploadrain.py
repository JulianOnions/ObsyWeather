
import os.path
import MyService
from googleapiclient.errors import HttpError
import sys

inputfile = "Rainfall.csv"
# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "14npA6zJtcD1d7foPzC6s7B4GiW52Hn8CVGyBHVFCkQo"
SAMPLE_RANGE_NAME = "Data!A2:C"

def main():
  try:
    service = MyService.getService()
    print("Service:", service)
    # appendValues(service)
    # Call the Sheets API
    sheet = service.spreadsheets()
    
    values = MyService.loadValuesBasic(inputfile)
    # print("Values:", values)
    body = {"values": values}
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
