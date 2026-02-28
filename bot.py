import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

LINK_ABBONAMENTO = "https://bit.ly/4aGlMn4"
LINK_ALICE = "https://t.me/Aliceunanessuna"
LINK_ZONAGIOCO = "https://bit.ly/4r1LVSc"

MESSAGGIO_BENVENUTO = """1️⃣ OPZIONE 
👉 Clicca opzione 1 nei bottoni sotto
💶 Paga: 12€
🎁 Ricevi:
🔓 Accesso al Gruppo Privato
⏳ Durata: 1 mese

2️⃣ OPZIONE 
👉 Clicca opzione 2 nei bottoni sotto ti registri, completi la registrazione
💶 Versa 20€
🎁 Ricevi:
🔓 Accesso al Gruppo Privato
⏳ Durata: 2 mesi
🎡 1 giro di ruota gratuito

3️⃣ OPZIONE 
👉 Clicca opzione 3 nei bottoni sotto ti registri, completi la registrazione
💶 Versa 20€
🎁 Ricevi:
🎡 3 giri di ruota gratuiti

⚠️ L'accesso e i bonus verranno attivati solo dopo verifica del pagamento e della registrazione (dove richiesta)"""

MESSAGGIO_RUOTA = "Ciao! 😘 registrati subito a Zona gioco ➡️ versa 20€, dopodiché contattami per la prova d'acquisto e otterrai subito i tuoi premi 🎁"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("1️⃣ OPZIONE", url=LINK_ABBONAMENTO)],
        [InlineKeyboardButton("2️⃣ OPZIONE", callback_data="plus")],
        [InlineKeyboardButton("3️⃣ OPZIONE", callback_data="play")],
    ]
    await update.message.reply_text(
        MESSAGGIO_BENVENUTO,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


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

    keyboard = [
        [InlineKeyboardButton("1️⃣ OPZIONE BASIC", url=LINK_ABBONAMENTO)],
        [InlineKeyboardButton("2️⃣ OPZIONE PLUS", callback_data="plus")],
        [InlineKeyboardButton("3️⃣ OPZIONE PLAY", callback_data="play")],
    ]
    await query.edit_message_text(
        text=MESSAGGIO_BENVENUTO,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(menu_handler, pattern="^menu$"))
    app.add_handler(CallbackQueryHandler(button_handler, pattern="^(plus|play)$"))
    print("Bot avviato! 🚀")
    app.run_polling()


if __name__ == "__main__":
    main()
