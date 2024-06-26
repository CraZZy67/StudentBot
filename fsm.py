# Обозначение состояний FSM с помощью наследования и добавление данных в словарь.

from aiogram.fsm.state import StatesGroup, State

from google_requests import gs

try:
    class AddState(StatesGroup):
        name = State()
        lesson = State()
        value_les = State()

        @staticmethod
        def add_in_sheet(data: list):
            data.append("Занятий еще не было")

            if len(gs.sheet_d) > 0 and gs.sheet_d != "empty":
                gs.sheet_d[f"{len(gs.sheet_d)}"] = data
            else:
                gs.sheet_d = {"0": data}

except Exception as ex:
    print(f"Возникла ошибка: {ex} в {__name__}")
