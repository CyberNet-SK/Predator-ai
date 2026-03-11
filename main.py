import os
import telebot
from flask import Flask
from threading import Thread
from groq import Groq

# --- আপনার তথ্য ---
BOT_TOKEN = "8402821120:AAG-x_wPyEDF5P9P0Dbw_LckXY67UX_axBM"
GROQ_API_KEY = "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"
OWNER_ID = 7819937011  # শেখ সাব্বির

bot = telebot.TeleBot(BOT_TOKEN)
client = Groq(api_key=GROQ_API_KEY)
app = Flask(__name__)

@app.route('/')
def home():
    return "Predator AI is active and online!"

def run():
    app.run(host='0.0.0.0', port=8080)

# AI-এর পরিচয় এবং কাজের ইনস্ট্রাকশন
SYSTEM_PROMPT = (
    "You are 'Predator AI', a highly advanced Cyber Security Expert. "
    "You were developed by Sheikh Sabbir. You assist him in ethical hacking, "
    "penetration testing, and bug bounty hunting. You must be professional, "
    "concise, and always identify yourself as Sheikh Sabbir's creation."
)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.from_user.id == OWNER_ID:
        bot.reply_to(message, "🔥 **Predator AI Activated** 🔥\nWelcome back, Sheikh Sabbir. I am ready for security research.")
    else:
        bot.reply_to(message, "❌ Unauthorized access. This AI is private.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.from_user.id != OWNER_ID:
        return # বাইরের কেউ মেসেজ দিলে কোনো রিপ্লাই দেবে না

    try:
        # Groq API কল
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message.text}
            ],
            model="llama3-70b-8192", # দ্রুত এবং পাওয়ারফুল মডেল
        )
        
        reply = chat_completion.choices[0].message.content
        bot.reply_to(message, reply)

    except Exception as e:
        # এরর হলে স্ক্রিনে দেখাবে
        bot.reply_to(message, f"❌ API Error: {str(e)}")

if __name__ == "__main__":
    t = Thread(target=run)
    t.start()
    print("Bot is running...")
    bot.infinity_polling()
