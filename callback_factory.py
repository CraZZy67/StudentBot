# Фабрика колбеков для более удобной обработки кнопок.

from aiogram.filters.callback_data import CallbackData


class CallbackStudent(CallbackData, prefix="stud"):
    type: str
    order: int
    name: str
