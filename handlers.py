""" Основной файл с обработчиками колбеков, состояний и команды /start.

Восемь первых обработчиков отвечают за машину состояния и отлавливания состояний которые в них же и назначаются.
Остальные обработчики выполняют функции подгрузки, сохранения и редактирования таблицы через ссылку на нее.
"""

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from icecream import ic

from keyboards import start_k, format_k, add_buttons_les, add_buttons_classes, confirm, understand
from fsm import AddState
from google_requests import gs
from settings import NUMBER_OF_CLASSES, LESSONS, NUMBER_OF_CLASSES_L, LESSONS_L, PERMISSION_ID

basic_router = Router()
ic.configureOutput(prefix="[INFO] ")
try:
    @basic_router.message(F.text == "/start")
    async def start(message: Message):
        if message.from_user.id in PERMISSION_ID:
            await message.answer("Выберите действие!", reply_markup=start_k())
        else:
            await message.answer("Этот бот вам недоступен =)")
        ic("Обработана команда старт")

    @basic_router.callback_query(F.data == "ADD")
    async def hand_adding(callback: CallbackQuery, state: FSMContext):
        await state.set_state(AddState.name)
        await callback.message.edit_text("Введите имя ученика которого вы хотите вписать в таблицу")
        await callback.answer()


    @basic_router.message(Command("cancel"))
    @basic_router.message(F.text.casefold() == "cancel")
    async def cancel_handler(message: Message, state: FSMContext):
        current_state = await state.get_state()
        if current_state is None:
            return

        await state.clear()
        await message.answer("Совершен выход", reply_markup=ReplyKeyboardRemove())
        await message.answer("Выберите действие!", reply_markup=start_k())
        ic("Обработан выход")

    @basic_router.message(AddState.name)
    async def catch_state_name(message: Message, state: FSMContext):
        await state.update_data(name=message.text)
        await state.set_state(AddState.lesson)
        await message.answer("Введите название предмета", reply_markup=add_buttons_les(LESSONS))
        ic("Имя добавлено")

    @basic_router.message(AddState.lesson, F.text.casefold().in_({*LESSONS_L}))
    async def catch_state_lesson(message: Message, state: FSMContext):
        await state.update_data(lesson=message.text)
        await state.set_state(AddState.value_les)
        await message.answer("Введите количество занятий", reply_markup=add_buttons_classes(NUMBER_OF_CLASSES))
        ic("Предмет добавлен")

    @basic_router.message(AddState.lesson)
    async def any_answer(message: Message):
        await message.reply("Выберите из предложенного =)")


    @basic_router.message(AddState.value_les, F.text.casefold().in_({*NUMBER_OF_CLASSES_L}))
    async def catch_state_value_les(message: Message, state: FSMContext):
        data = await state.update_data(value_ls=message.text)
        AddState.add_in_sheet([data["name"], data["lesson"], f"{0}/" + data["value_ls"]])
        await state.clear()
        await message.answer("Информация записана в таблицу", reply_markup=ReplyKeyboardRemove())
        await message.answer("Выберите действие!", reply_markup=start_k())
        ic("Количество занятий добавлено")

    @basic_router.message(AddState.value_les)
    async def any_answer(message: Message):
        await message.reply("Выберите из предложенного =)")


    @basic_router.callback_query(F.data.in_({"FORMATTING", "BACK_TO_START"}))
    async def handling_format(callback: CallbackQuery):
        if callback.data == "FORMATTING":
            await callback.message.edit_text("Ссылка для редактирования таблицы:", reply_markup=format_k())
        else:
            await callback.message.edit_text("Выберите действие!", reply_markup=start_k())
        ic("Обработано редактирование")

    @basic_router.callback_query(F.data.in_({"SAVE_CHANGES", "LOAD_SHEET"}))
    async def handling_format(callback: CallbackQuery):
        if callback.data == "LOAD_SHEET":
            await callback.message.edit_text("Вы уверенны в том что хотите загрузить таблицу? "
                                             "Все не сохраненные изменения будут потеряны!", reply_markup=confirm(data="CONFIRM"))
        else:
            gs.update_sheet(gs.sheet_d)
            await callback.message.answer("Изменения успешно сохранены!", reply_markup=understand())
            await callback.answer()
        ic("Обработано: {SAVE_CHANGES, LOAD_SHEET}")

    @basic_router.callback_query(F.data.in_({"UNDERSTAND", "CONFIRM", "CANCEL"}))
    async def handling_confirm(callback: CallbackQuery):

        if callback.data == "UNDERSTAND":
            await callback.message.delete()

        elif callback.data == "CONFIRM":
            gs.get_sheet()
            await callback.message.edit_text("Выберите действие!", reply_markup=start_k())
            await callback.message.answer("Таблица успешно загружена!", reply_markup=understand())

        else:
            await callback.message.edit_text("Выберите действие!", reply_markup=start_k())
        ic("Обработано: {UNDERSTAND, CONFIRM, CANCEL}")

except Exception as ex:
    print(f"Возникла ошибка: {ex}, в {__name__}")
