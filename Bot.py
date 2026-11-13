import requests
import os
from datetime import datetime

# DO NOT EDIT THIS LINE - Token comes from GitHub Secrets
BOT_TOKEN =9171651303:AAGSXC9oIu08e7rX2WdrBtaJzyDZJsChphg
CHANNEL_ID = "@Officialctboybot"

# You can add more symbols here
SYMBOLS = ["TSLA", "AAPL", "GC=F", "BTC-USD"]

def get_price(symbol):
    try:
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=headers, timeout=10).json()
        meta = r['chart']['result'][0]['meta']
        price = meta['regularMarketPrice']
        change = meta.get('regularMarketChangePercent', 0)
        return price, change
    except:
        return None, None

def send_msg(text):
    url = f"https://api.telegram.org/bot{9171651303:AAGSXC9oIu08e7rX2WdrBtaJzyDZJsChphg }/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,https://t.me/Dailyotcstock
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": True
    }
    requests.post(url, data=payload)

# Time
now = datetime.now().strftime("%H:%M UTC - %d %b")

for sym in SYMBOLS:
    price, chg = get_price(sym)
    if price:
        emoji = "🟢" if chg > 0 else "🔴"
        msg = f"""{emoji} *MARKET SCAN - {now}*

*Asset:* {sym}
*Live Price:* ${price:.2f}
*Daily Change:* {chg:.2f}%

*Source:* Yahoo Finance
*Type:* Educational Scanner

Risk Warning: Trading is risky. Not financial advice. Use demo.

Learn: https://one.toexness.com/a/0vfuuobnsg

Bot: @Officialctboybot
"""
        send_msg(msg)

print("Scan sent!")
