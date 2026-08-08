from telegram import Update
from telegram.ext import Application, ChatJoinRequestHandler, ContextTypes

BOT_TOKEN = "8712036849:AAFMM7lvkNxG71VsY-vEjPr5Zkns9uJBg8Y
"

async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.chat_join_request:
        await update.chat_join_request.approve()
        print(f"Approved: {update.chat_join_request.from_user.full_name}")

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(ChatJoinRequestHandler(approve))

print("Bot ishga tushdi...")
app.run_polling()
