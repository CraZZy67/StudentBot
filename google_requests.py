import gspread
from icecream import ic

from settings import NAME_TABLE


ic.configureOutput(prefix="[INFO] ")


class GoogleRequests:
    def __init__(self):
        self.sheet_d = None
        self.gs = gspread.service_account(filename="credentials.json")
        self.wks = self.gs.open(f"{NAME_TABLE}").sheet1

    def get_sheet(self):
        count = 0
        sheet_dict = dict()
        values = self.wks.get("A2:D")
        if len(values[0]) != 0:
            for row in values:
                sheet_dict[str(count)] = row
                count += 1
        else:
            ic("Пустая таблица или таблица с пробелом будет ровняться значению empty!")

        ic("Таблица успешно извлечена!")
        self.sheet_d = sheet_dict if len(sheet_dict) > 0 else "empty"

    def update_sheet(self, sheet_dict: dict):
        values = []
        if len(sheet_dict) > 0 and sheet_dict != "empty":
            for v in sheet_dict.values():
                values.append(v)

        self.wks.batch_clear(["A2:D"])
        ic("Таблица успешно отчищена!")

        if len(values) > 0:
            self.wks.update(values, "A2:D")
        ic("Таблица успешно обновлена!")


gs = GoogleRequests()
gs.get_sheet()
