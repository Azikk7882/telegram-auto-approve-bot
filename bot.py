import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import ChatJoinRequest

from config import BOT_TOKEN
from database import init_db, add_user

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.chat_join_request()
async def approve_join_request(request: ChatJoinRequest):
    await bot.approve_chat_join_request(
        chat_id=request.chat.id,
        user_id=request.from_user.id
    )

    await add_user(
        user_id=request.from_user.id,
        username=request.from_user.username,
        full_name=request.from_user.full_name
    )


async def main():
    await init_db()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
