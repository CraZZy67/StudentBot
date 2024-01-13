import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from icecream import ic

from settings import SCOPES, ID_SHEET, NAME_LIST


ic.configureOutput(prefix="[INFO] ")


class GoogleRequests:
    def __init__(self):

        self.creds = None
        self.service = None
        self.sheet_d = None

        if os.path.exists("token.json"):
            self.creds = Credentials.from_authorized_user_file("token.json", SCOPES)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                  "credentials.json", SCOPES
                )
                self.creds = flow.run_local_server(port=0)

            with open("token.json", "w") as token:
                token.write(self.creds.to_json())

    def get_sheet(self):
        try:
            count = 0
            sheet_dict = dict()

            self.service = build("sheets", "v4", credentials=self.creds)

            sheet = self.service.spreadsheets()
            result = (sheet.values().get(spreadsheetId=ID_SHEET, range=f"{NAME_LIST}!A2:D").execute())
            values = result.get("values", [])

            for row in values:
                sheet_dict[str(count)] = row
                count += 1
            count = 0
            ic("Таблица успешно извлечена!")
            self.sheet_d = sheet_dict if len(sheet_dict) > 0 else "empty"

        except HttpError as err:
            print(err)

    def update_sheet(self, sheet_dict: dict):

        try:
            values = []
            if len(sheet_dict) > 0 and sheet_dict != "empty":
                for v in sheet_dict.values():
                    values.append(v)

            self.service = build("sheets", "v4", credentials=self.creds)
            sheet = self.service.spreadsheets()

            sheet.values().clear(spreadsheetId=ID_SHEET, range=f"{NAME_LIST}!A2:D").execute()
            ic("Таблица успешно отчищена!")

            if len(values) > 0:
                (sheet.values().update(spreadsheetId=ID_SHEET, range=f"{NAME_LIST}!A2:D",
                                       valueInputOption="USER_ENTERED", body={"values": values}).execute())

                ic("Таблица успешно обновлена!")

        except HttpError as err:
            print(err)


gs = GoogleRequests()
gs.get_sheet()
