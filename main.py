import os
import telebot
from flask import Flask
from threading import Thread
from groq import Groq

# --- CONFIGURATION ---
BOT_TOKEN = "8402821120:AAG-x_wPyEDF5P9P0Dbw_LckXY67UX_axBM"
GROQ_API_KEY = "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"
OWNER_ID = 7819937011  # Sheikh Sabbir's ID

bot = telebot.TeleBot(BOT_TOKEN)
client = Groq(api_key=GROQ_API_KEY)
app = Flask(__name__)

# --- WEB SERVER FOR RENDER ---
@app.route('/')
def home():
    return "Predator AI is Running 24/7!"

def run():
    app.run(host='0.0.0.0', port=8080)

# --- AI LOGIC ---
SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are Predator AI, a Cyber Security Expert. Created by Sheikh Sabbir. "
        "You help with penetration testing and bug bounty. You must answer in Bengali and English. "
        "If anyone asks about your creator, say: 'I am a Cyber Security Expert AI, developed by Sheikh Sabbir.'"
    )
}

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Only allow Sheikh Sabbir to use the bot (Optional Security)
    if message.from_user.id != OWNER_ID:
        bot.reply_to(message, "Sorry, this AI is private and only accessible by Sheikh Sabbir.")
        return

    try:
        chat_completion = client.chat.completions.create(
            messages=[SYSTEM_PROMPT, {"role": "user", "content": message.text}],
            model="llama3-8b-8192",
        )
        response = chat_completion.choices[0].message.content
        bot.reply_to(message, response)
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

# --- START BOT ---
if __name__ == "__main__":
    print("Bot is starting...")
    t = Thread(target=run)
    t.start()
    bot.infinity_polling()
