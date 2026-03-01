import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

LINK_ABBONAMENTO = "https://bit.ly/4aGlMn4"
LINK_ALICE = "https://t.me/Aliceunanessuna"
LINK_ZONAGIOCO = "https://bit.ly/4r1LVSc"

MSG_1 = """1️⃣ OPZIONE 
👉 Clicca il bottone opzione 1
💶 Paga: 12€
🎁 Ricevi:
🔓 Accesso al Gruppo Privato
⏳ Durata: 1 mese"""

MSG_2 = """2️⃣ OPZIONE 
👉 Clicca il bottone opzione 2 ti registri, completi la registrazione
💶 Versa 20€
🎁 Ricevi:
🔓 Accesso al Gruppo Privato
⏳ Durata: 2 mesi
🎡 1 giro di ruota gratuito"""

MSG_3 = """3️⃣ OPZIONE 
👉 Clicca il bottone opzione 3 ti registri, completi la registrazione
💶 Versa 20€
🎁 Ricevi:
🎡 3 giri di ruota gratuiti"""

MESSAGGIO_RUOTA = "Ciao! 😘 registrati subito a Zona gioco ➡️ versa 20€, dopodiché contattami per la prova d'acquisto e otterrai subito i tuoi premi 🎁"


async def send_menu(message):
    kb1 = [[InlineKeyboardButton("1️⃣ OPZIONE", url=LINK_ABBONAMENTO)]]
    await message.reply_text(MSG_1, reply_markup=InlineKeyboardMarkup(kb1))

    kb2 = [[InlineKeyboardButton("2️⃣ OPZIONE", callback_data="plus")]]
    await message.reply_text(MSG_2, reply_markup=InlineKeyboardMarkup(kb2))

    kb3 = [[InlineKeyboardButton("3️⃣ OPZIONE", callback_data="play")]]
    await message.reply_text(MSG_3, reply_markup=InlineKeyboardMarkup(kb3))


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_menu(update.message)


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("🔗 Contattami", url=LINK_ALICE)],
        [InlineKeyboardButton("🎰 Registrati su Zona Gioco", url=LINK_ZONAGIOCO)],
        [InlineKeyboardButton("⬅️ Torna al menu", callback_data="menu")],
    ]
    await query.edit_message_text(
        text=MESSAGGIO_RUOTA,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await send_menu(query.message)


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(menu_handler, pattern="^menu$"))
    app.add_handler(CallbackQueryHandler(button_handler, pattern="^(plus|play)$"))
    print("Bot avviato! 🚀")
    app.run_polling()


if __name__ == "__main__":
    main()
