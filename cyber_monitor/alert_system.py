import smtplib
import requests
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "knamiq605@gmail.com"  # Buraya öz e-poçt ünvanınızı yazın
EMAIL_PASSWORD = "06.10.2003"  # Buraya parolunuzu yazın
EMAIL_RECEIVER = "knamiq605@gmail.com"  # Buraya alıcının e-poçt ünvanını yazın

def send_email_alert(message):
    msg = MIMEText(message)
    msg["Subject"] = "🚨 Cyber Security Alert!"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()
        print("✅ Email alert sent!")
    except Exception as e:
        print(f"❌ Email alert failed: {e}")

# Telegram Alert Sistemi
TELEGRAM_BOT_TOKEN = "your_bot_token"  # Bot tokeninizi burada yazın
TELEGRAM_CHAT_ID = "your_chat_id"  # Telegram chat ID-ni burada yazın

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("✅ Telegram alert sent!")
        else:
            print("❌ Telegram alert failed!")
    except Exception as e:
        print(f"❌ Telegram alert error: {e}")
