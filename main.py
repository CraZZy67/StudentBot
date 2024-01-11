from asyncio import run

from create_bot import bot, dp
from handlers import basic_router

dp.include_routers(basic_router)

try:
    async def main():
        await dp.start_polling(bot)

    if __name__ == "__main__":
        print("Бот запущен!")
        run(main())

except Exception as ex:
    print(f"Возникла ошибка: {ex}, в {__name__}")