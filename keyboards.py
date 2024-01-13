from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, ReplyKeyboardMarkup

from settings import URL_TABLE
from callback_factory import CallbackStudent

try:
    def start_k():
        start_kb = InlineKeyboardBuilder()

        start_kb.add(InlineKeyboardButton(text="Добавить", callback_data="ADD"),
                     InlineKeyboardButton(text="Удалить", callback_data="DELETE"))
        start_kb.add(InlineKeyboardButton(text="Лист", callback_data="LIST"),
                     InlineKeyboardButton(text="Редактировать", callback_data="FORMATTING"))
        start_kb.add(InlineKeyboardButton(text="Сохранить изменения", callback_data="SAVE_CHANGES"),
                     InlineKeyboardButton(text="Загрузить таблицу", callback_data="LOAD_SHEET"))
        start_kb.adjust(2, 2, 2)
        return start_kb.as_markup()


    def add_buttons_les(list_name):

        lessons_kb = ReplyKeyboardMarkup(keyboard=list_name, resize_keyboard=True)
        return lessons_kb


    def add_buttons_classes(list_name):

        classes_kb = ReplyKeyboardMarkup(keyboard=list_name, resize_keyboard=True)
        return classes_kb


    def format_k():
        format_kb = InlineKeyboardBuilder()
        format_kb.add(InlineKeyboardButton(text="Гугл таблица", url=URL_TABLE),
                      InlineKeyboardButton(text="Назад", callback_data="BACK_TO_START"))
        format_kb.adjust(1, 1)
        return format_kb.as_markup()

    def confirm(data: str):
        builder_confirm = InlineKeyboardBuilder()
        builder_confirm.add(InlineKeyboardButton(text="Подтвердить", callback_data=data),
                            InlineKeyboardButton(text="Отмена", callback_data="CANCEL"))
        builder_confirm.adjust(2)

        return builder_confirm.as_markup()


    def understand():
        builder_understand = InlineKeyboardBuilder()
        builder_understand.add(InlineKeyboardButton(text="Понятно", callback_data="UNDERSTAND"))

        return builder_understand.as_markup()

    def kb_for_list(sheet: dict, view: str):
        list_builder = InlineKeyboardBuilder()
        if len(sheet) > 0 and sheet != "empty":

            count_line = 1

            for value in sheet.values():
                list_builder.button(text=f"{count_line}. {value[0]}",
                                    callback_data=CallbackStudent(type=view, order=count_line, name=f"{value[0]}")
                                    )
                count_line += 1

            list_builder.button(text="Назад", callback_data="BACK")
            list_builder.adjust(*[2] * count_line)
            return list_builder.as_markup()

        list_builder.button(text="Назад", callback_data="BACK")
        return list_builder.as_markup()

except Exception as ex:
    print(f"Возникла ошибка: {ex}, в {__name__}")
