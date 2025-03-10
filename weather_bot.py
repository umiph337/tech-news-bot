import feedparser
import requests
import os

URL = "https://vnexpress.net/rss/cong-nghe.rss"

def get_weather_news():
    feed = feedparser.parse(URL)
    articles = []
    for entry in feed.entries[:3]:  # Get top 3 articles for testing
        summary = entry.summary.split(". ")[0]  # Get first sentence
        articles.append({"title": entry.title, "summary": summary, "link": entry.link})
    return articles

import re

def escape_markdown(text):
    """Escapes special Markdown characters for Telegram"""
    escape_chars = r'_*[]()~`>#+-=|{}.!'
    return "".join(f"\\{char}" if char in escape_chars else char for char in text)

def format_news(news):
    message = "🌤️ *Daily Weather News Summary* 🌤️\n\n"
    for item in news:
        title = escape_markdown(item['title'])
        summary = escape_markdown(item['summary'])
        link = item['link']  # No need to escape links

        message += f"🔹 *{title}*\n📌 {summary}...\n🔗 [Read more]({link})\n\n"
    return message

def send_telegram_message(message):
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    response = requests.post(url, json=payload)
    print("Telegram API Response:", response.json())  # Print response for debugging
    return response.json()

# Run script
news = get_weather_news()
summary_message = format_news(news)
send_telegram_message(summary_message)

