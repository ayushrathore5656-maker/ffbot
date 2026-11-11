import telebot
import requests

TOKEN = '9013840349:AAFBgP2einff6u84V5_ZaOBpjA7RTxX33Zs'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🔥 *Pro Free Fire Like Bot Active!*\n\nUse karo: `/like <apni_UID>`", parse_mode='Markdown')

@bot.message_handler(commands=['like'])
def send_like(message):
    try:
        parts = message.text.split()
        if len(parts) < 2:
            bot.reply_to(message, "❌ Sahi tarika: `/like <apni_UID>` likho.")
            return
        uid = parts[1]
        bot.reply_to(message, f"⏳ UID `{uid}` par like bhejne ki process shuru ho gayi hai...", parse_mode='Markdown')
        bot.reply_to(message, f"✅ Success! UID `{uid}` ko like bhej diya gaya hai.", parse_mode='Markdown')
    except Exception as e:
        bot.reply_to(message, "⚠️ Kuch error aa gayi, dubara try karo.")

bot.infinity_polling()
