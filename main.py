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
    "You were developed by Sheikh Sabbir. You assist him in security research, "
    "penetration testing, and bug bounty hunting. Answer in Bengali or English as requested. "
    "If anyone asks who created you, proudly say: 'I am a Cyber Security Expert AI, developed by Sheikh Sabbir.'"
)

# --- COMMANDS ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.from_user.id == OWNER_ID:
        welcome_text = (
            "🔥 **Predator AI Activated** 🔥\n"
            "----------------------------\n"
            "I am a Cyber Security Expert AI, developed by Sheikh Sabbir.\n"
            "I am here to assist with Penetration Testing and Security Analysis.\n\n"
            "Commands:\n"
            "/start - Initialize the bot\n"
            "/help - Show help menu\n"
            "/status - Check bot status"
        )
        bot.reply_to(message, welcome_text, parse_mode="Markdown")
    else:
        bot.reply_to(message, "❌ Unauthorized access. This AI is private.")

@bot.message_handler(commands=['status'])
def status_check(message):
    bot.reply_to(message, "✅ Predator AI is Online and Operational.")

@bot.message_handler(commands=['help'])
def help_menu(message):
    help_text = (
        "🛠 **Predator AI Help Menu** 🛠\n"
        "----------------------------\n"
        "Ask me about:\n"
        "- Network Security & Nmap\n"
        "- Web Vulnerabilities (SQLi, XSS, etc.)\n"
        "- Exploit Development\n"
        "- Automation Scripts"
    )
    bot.reply_to(message, help_text, parse_mode="Markdown")

# --- AI CHAT LOGIC ---
@bot.message_handler(func=lambda message: True)
def handle_ai_chat(message):
    if message.from_user.id != OWNER_ID:
        return

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message.text}
            ],
            model="llama3-8b-8192",
        )
        reply = chat_completion.choices[0].message.content
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {str(e)}")

if __name__ == "__main__":
    t = Thread(target=run)
    t.start()
    print("Bot is starting...")
    bot.infinity_polling()
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "🛠 Ask me about SQLi, XSS, Nmap, or any Security topics.")

@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(message, "✅ System is Operational.")

# --- মূল চ্যাট লজিক যেখানে এরর হচ্ছে ---
@bot.message_handler(func=lambda message: True)
def chat(message):
    if message.from_user.id != OWNER_ID:
        return

    try:
        # মডেল হিসেবে 'llama3-8b-8192' ব্যবহার করা হয়েছে যা সবচেয়ে স্টেবল
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message.text}
            ],
            temperature=0.7,
            max_tokens=1024,
        )
        
        ans = completion.choices[0].message.content
        bot.reply_to(message, ans)

    except Exception as e:
        # এরর হলে আসল কারণটি টেলিগ্রামে দেখাবে
        bot.reply_to(message, f"❌ API Error Details: {str(e)}")

if __name__ == "__main__":
    t = Thread(target=run)
    t.start()
    bot.infinity_polling()
            "🔥 **Predator AI Activated** 🔥\n"
            "----------------------------\n"
            "I am a Cyber Security Expert AI, developed by Sheikh Sabbir.\n"
            "I am here to assist with Penetration Testing and Security Analysis.\n\n"
            "Commands:\n"
            "/start - Initialize the bot\n"
            "/help - Show help menu\n"
            "/status - Check bot status"
        )
        bot.reply_to(message, welcome_text, parse_mode="Markdown")
    else:
        bot.reply_to(message, "❌ Unauthorized access. This AI is private.")

@bot.message_handler(commands=['status'])
def status_check(message):
    bot.reply_to(message, "✅ Predator AI is Online and Operational.")

@bot.message_handler(commands=['help'])
def help_menu(message):
    help_text = (
        "🛠 **Predator AI Help Menu** 🛠\n"
        "----------------------------\n"
        "Ask me about:\n"
        "- Network Security & Nmap\n"
        "- Web Vulnerabilities (SQLi, XSS, etc.)\n"
        "- Exploit Development\n"
        "- Automation Scripts"
    )
    bot.reply_to(message, help_text, parse_mode="Markdown")

# --- AI CHAT LOGIC ---
@bot.message_handler(func=lambda message: True)
def handle_ai_chat(message):
    # শুধুমাত্র শেখ সাব্বির মেসেজ দিলে রিপ্লাই দেবে
    if message.from_user.id != OWNER_ID:
        return

    try:
        # Groq API কল করার সময় মডেল নাম চেক করুন
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message.text}
            ],
            model="llama3-8b-8192", # দ্রুত এবং স্টেবল মডেল
        )
        
        reply = chat_completion.choices[0].message.content
        bot.reply_to(message, reply)

    except Exception as e:
        # এরর মেসেজটি ডিটেইলসে দেখাবে
        error_msg = f"❌ Error: {str(e)}"
        bot.reply_to(message, error_msg)

if __name__ == "__main__":
    t = Thread(target=run)
    t.start()
    print("Bot is starting...")
    bot.infinity_polling()
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
