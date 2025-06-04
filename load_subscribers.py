import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_subscriber():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open("Daily-NewsDigest Subscribers").sheet1

    emails = sheet.col_values(1)[1:]
    return tuple(set(emails))
