import feedparser
import requests
import os

# Step 1: Fetch Weather News from RSS Feed
URL = "https://vnexpress.net/rss/cong-nghe.rss"

def get_weather_news():
    feed = feedparser.parse(URL)
    articles = []
    for entry in feed.entries:
        summary = entry.summary.split(". ")[0]  # Take the first sentence as summary
        articles.append({"title": entry.title, "summary": summary, "link": entry.link})
    return articles

# Step 2: Format the News Summary
def format_news(news):
    message = "🌤️ *Daily Weather News Summary* 🌤️\n\n"
    for item in news:
        message += f"🔹 *{item['title']}*\n📌 {item['summary']}...\n🔗 [Read more]({item['link']})\n\n"
    return message

# Step 3: Send Summary to Telegram
def send_telegram_message(message):
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Securely stored in GitHub Secrets
    CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    response = requests.post(url, json=payload)
    return response.json()

# Run the script
news = get_weather_news()
summary_message = format_news(news)
send_telegram_message(summary_message)

print("✅ Sent to Telegram!")
