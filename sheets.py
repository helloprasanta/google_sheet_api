import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Google_Sheet_API_Test").sheet1

# Get All Sheet Data
data = sheet.get_all_records()
pprint(data)

# Get Row Data At Particular Row
row = sheet.row_values(3)
# pprint(row)

# Get Col Data At Particular Col
col = sheet.col_values(3)
# pprint(col)

# insertRow = ["Hello", 5, "Red", "Blue"]
# sheet.update_cell(2, 2, "CHANGED")
insertRow = ["5", "RAMESH", 80]
sheet.insert_row(insertRow, 6)


sheet.delete_row(2)
pprint("The row has been deleted")
