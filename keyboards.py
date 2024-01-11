from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, ReplyKeyboardMarkup

from settings import URL_TABLE

try:

    start_kb = InlineKeyboardBuilder()

    start_kb.add(InlineKeyboardButton(text="Добавить", callback_data="ADD"),
                 InlineKeyboardButton(text="Удалить", callback_data="DELETE"))
    start_kb.add(InlineKeyboardButton(text="Лист", callback_data="LIST"),
                 InlineKeyboardButton(text="Редактировать", callback_data="FORMATTING"))
    start_kb.add(InlineKeyboardButton(text="Сохранить изменения", callback_data="SAVE_CHANGES"),
                 InlineKeyboardButton(text="Загрузить таблицу", callback_data="LOAD_SHEET"))
    start_kb.adjust(2, 2, 2)


    def add_buttons_les(list_name):

        lessons_kb = ReplyKeyboardMarkup(keyboard=list_name, resize_keyboard=True)
        return lessons_kb


    def add_buttons_classes(list_name):

        classes_kb = ReplyKeyboardMarkup(keyboard=list_name, resize_keyboard=True)
        return classes_kb


    format_kb = InlineKeyboardBuilder()
    format_kb.add(InlineKeyboardButton(text="Гугл таблица", url=URL_TABLE),
                  InlineKeyboardButton(text="Назад", callback_data="BACK_TO_START"))
    format_kb.adjust(1, 1)


except Exception as ex:
    print(f"Возникла ошибка: {ex}, в {__name__}")
