from asyncio import run

from create_bot import bot, dp

dp.include_routers(...)

try:
    async def main():
        await dp.start_polling(bot)

    if __name__ == "__main__":
        print("Бот запущен!")
        run(main())

except Exception as ex:
    print(f"Возникла ошибка: {ex}, в {__name__}")