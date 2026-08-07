from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🖥 Mahsulotlar"),
            KeyboardButton(text="🔥 Aksiyalar")
        ],
        [
            KeyboardButton(text="🛒 Buyurtma berish")
        ],
        [
            KeyboardButton(text="📦 Yetkazib berish"),
            KeyboardButton(text="☎️ Aloqa")
        ]
    ],
    resize_keyboard=True
)
