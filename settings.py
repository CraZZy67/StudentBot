""" Объявление глобальных констант и их настройка под пользователя.

При желании добавить или удалить количества занятий или сами занятия нужно изменить две переменных.
Пример:
LESSONS_L = ["roblox", "web", "minecraft", "unity", "..."]
LESSONS = \
 [
    [
        KeyboardButton(text="Roblox"),
        KeyboardButton(text="Web"),
        KeyboardButton(text="Minecraft"),
        KeyboardButton(text="Unity"),
        KeyboardButton(text="Занятие которое вы хотите добавить") +
    ]
 ]

 Аналогичные действия совершаются с количеством занятий.
"""

from aiogram.utils.keyboard import KeyboardButton

ID_SHEET = "1eCD4AWihcoPY_KgiNNX6kRkFHHHdWpps3OeUvFL2w_0"
NAME_LIST = "StudentINF"
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
LESSONS_L = ["roblox", "web", "minecraft", "unity"]  # список доступных занятий (менять вместе с нижним вложенным списком)
LESSONS = \
 [
    [
        KeyboardButton(text="Roblox"),
        KeyboardButton(text="Web"),
        KeyboardButton(text="Minecraft"),
        KeyboardButton(text="Unity"),
    ]
 ]
NUMBER_OF_CLASSES_L = ["4", "6"]  # список количества занятий (менять вместе с нижним вложенным списком)
NUMBER_OF_CLASSES = \
 [
    [
        KeyboardButton(text="4"),
        KeyboardButton(text="6")
    ]
 ]
DELIMITER = "—————————————————————————"  # разделитель в списке учеников
PERMISSION_ID = [1162899410]
URL_TABLE = "https://docs.google.com/spreadsheets/d/1eCD4AWihcoPY_KgiNNX6kRkFHHHdWpps3OeUvFL2w_0/edit#gid=0"
