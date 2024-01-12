from aiogram import F, Router
from aiogram.types import CallbackQuery

from google_requests import gs
from secondary_fuctions import formatting_text
from keyboards import kb_for_list, start_kb

additional_router = Router()


@additional_router.callback_query(F.data.in_({"LIST", "DELETE", "BACK"}))
async def handl_list(callback: CallbackQuery):
    if callback.data == "LIST":
        await callback.message.edit_text(text=formatting_text(gs.sheet_d), reply_markup=kb_for_list(gs.sheet_d))
    if callback.data == "BACK":
        await callback.message.edit_text("Выберите действие!", reply_markup=start_kb.as_markup())
