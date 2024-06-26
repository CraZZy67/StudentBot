# Основной исполняемый файл, где происходит запуск бота.

from asyncio import run
from icecream import ic

from create_bot import bot, dp
from handlers import basic_router
from handlers_second import additional_router

ic.configureOutput(prefix="[INFO] ")
dp.include_routers(basic_router, additional_router)

try:
    async def main():
        await dp.start_polling(bot)

    if __name__ == "__main__":
        ic("Бот запущен!")
        run(main())

except Exception as ex:
    print(f"Возникла ошибка: {ex}, в {__name__}")
