from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

categories_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⌨️ Klaviaturalar"),
            KeyboardButton(text="🖱 Sichqonchalar")
        ],
        [
            KeyboardButton(text="🎧 Quloqchinlar"),
            KeyboardButton(text="🖥 Monitorlar")
        ],
        [
            KeyboardButton(text="🎮 Gaming aksessuarlar")
        ],
        [
            KeyboardButton(text="🔙 Orqaga")
        ]
    ],
    resize_keyboard=True
)
