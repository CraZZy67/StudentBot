# Реализованны обработки кнопок добавления занятий и их удаления.

from datetime import datetime

from aiogram import F, Router
from aiogram.types import CallbackQuery
from icecream import ic

from google_requests import gs
from secondary_fuctions import formatting_text, add_exam_value, shuffle
from keyboards import kb_for_list, start_k
from callback_factory import CallbackStudent

additional_router = Router()
ic.configureOutput(prefix="[INFO] ")
try:
    @additional_router.callback_query(F.data.in_({"LIST", "DELETE", "BACK"}))
    async def handl_list(callback: CallbackQuery):
        if callback.data == "LIST":
            await callback.message.edit_text(text=formatting_text(gs.sheet_d), reply_markup=kb_for_list(gs.sheet_d, view="list"))
        elif callback.data == "BACK":
            await callback.message.edit_text("Выберите действие!", reply_markup=start_k())
        else:
            await callback.message.edit_text(text=formatting_text(gs.sheet_d), reply_markup=kb_for_list(gs.sheet_d, view="delete"))
        ic("Обработано: {LIST, DELETE, BACK}")

    @additional_router.callback_query(CallbackStudent.filter(F.type == "list"))
    async def handl_buttons_l(callback: CallbackQuery, callback_data: CallbackStudent):
        string_or_finish = add_exam_value(gs.sheet_d[f"{callback_data.order - 1}"][2])

        if string_or_finish != "finish":
            gs.sheet_d[f"{callback_data.order - 1}"][2] = string_or_finish

            if gs.sheet_d[f"{callback_data.order - 1}"][3] == "Занятий еще не было":
                gs.sheet_d[f"{callback_data.order - 1}"][3] = f"{datetime.now().date()}, "
            else:
                gs.sheet_d[f"{callback_data.order - 1}"][3] += f"{datetime.now().date()}, "

            await callback.message.edit_text(text=formatting_text(gs.sheet_d), reply_markup=kb_for_list(gs.sheet_d, view="list"))
        else:

            gs.sheet_d[f"{callback_data.order - 1}"][3] += str(datetime.now().date())
            await callback.message.delete()
            await callback.message.answer("Курс окончен!")
            await callback.message.answer(f"Имя: {gs.sheet_d[str(callback_data.order - 1)][0]} | Предмет: {gs.sheet_d[str(callback_data.order - 1)][1]} | "
                                          f"Уроков: {gs.sheet_d[str(callback_data.order - 1)][2][2]}\nДаты: {gs.sheet_d[str(callback_data.order - 1)][3]}")
            gs.sheet_d[f"{callback_data.order - 1}"][3] = "Занятий еще не было"
            gs.sheet_d[f"{callback_data.order - 1}"][2] = f"0/{gs.sheet_d[str(callback_data.order - 1)][2][2]}"
            await callback.message.answer(text=formatting_text(gs.sheet_d), reply_markup=kb_for_list(gs.sheet_d, view="list"))
        ic("Обработана кнопка списка")

    @additional_router.callback_query(CallbackStudent.filter(F.type == "delete"))
    async def handl_buttons_d(callback: CallbackQuery, callback_data: CallbackStudent):
        gs.sheet_d.pop(f"{callback_data.order - 1}")
        gs.sheet_d = shuffle(gs.sheet_d)
        await callback.message.edit_text(text=formatting_text(gs.sheet_d), reply_markup=kb_for_list(gs.sheet_d, view="delete"))
        ic("Обработана кнопка удаления")

except Exception as ex:
    print(f"Возникла ошибка: {ex}, в {__name__}")
