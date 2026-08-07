from aiogram import Router
from aiogram.types import ChatJoinRequest, Message

from database import add_user, total_users

router = Router()


@router.chat_join_request()
async def approve_request(request: ChatJoinRequest):
    await request.approve()

    await add_user(
        user_id=request.from_user.id,
        username=request.from_user.username or "",
        full_name=request.from_user.full_name
    )


@router.message(lambda message: message.text == "/stats")
async def stats(message: Message):
    users = await total_users()

    await message.answer(
        f"📊 Bot statistikasi\n\n"
        f"👥 Jami foydalanuvchilar: {users}"
    )
