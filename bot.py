from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8522852514:AAHwoF3nh74T8kEwXzygcuHnPESeEZrr95A"

WEBSITE_URL = "https://google.com"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔗 LINK", url=WEBSITE_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    username = update.effective_user.username or "User"

    await update.message.reply_photo(
        photo=open("logo.png", "rb"),
        caption=f"👋 Hello {username},\n\nYour account isn't linked with our website.",
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
