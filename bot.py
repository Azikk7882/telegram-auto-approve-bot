import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import ChatJoinRequest

from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.chat_join_request()
async def approve(request: ChatJoinRequest):
    await request.approve()
    print(f"Approved: {request.from_user.full_name}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
