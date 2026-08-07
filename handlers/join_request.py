from aiogram import Router
from aiogram.types import ChatJoinRequest

router = Router()


@router.chat_join_request()
async def approve_join(request: ChatJoinRequest):
    await request.approve()

    await request.user.send_message(
        "✅ Kanalga xush kelibsiz!"
    )
