import requests
import os
import feedparser
import html

# Load environment variables (Telegram bot token & chat ID)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Weather news RSS feed URL (Replace with actual feed)
RSS_FEED_URL = "https://vnexpress.net/rss/cong-nghe.rss"

def get_weather_news():
    """Fetches weather news from an RSS feed and returns a list of news items."""
    feed = feedparser.parse(RSS_FEED_URL)
    news_list = []

    for entry in feed.entries[:10]:  # Increased to 10 news articles
        news_list.append({
            "title": entry.title,
            "summary": entry.summary.split("</a>")[-1].strip(),  # Remove embedded links
            "link": entry.link
        })

    return news_list

def format_news(news):
    """Formats the news list into a Telegram-friendly message using HTML."""
    message = "🌤️ <b>Daily Weather News Summary</b> 🌤️\n\n"

    for item in news:
        title = html.escape(item['title'])  # Escape HTML characters
        summary = html.escape(item['summary'])  # Escape HTML characters
        link = item['link']  # No need to escape links

        message += f"🔹 <b>{title}</b>\n📌 {summary}...\n🔗 <a href=\"{link}\">Read more</a>\n\n"
    
    return message.strip()

def send_telegram_message(message):
    """Sends a formatted message to Telegram."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML",  # Use HTML mode for formatting
        "disable_web_page_preview": False  # Enable rich link preview
    }
    
    response = requests.post(url, json=payload)
    print("Telegram API Response:", response.json())  # Debugging
    return response.json()

if __name__ == "__main__":
    weather_news = get_weather_news()
    
    if weather_news:
        formatted_message = format_news(weather_news)
        send_telegram_message(formatted_message)
    else:
        print("No weather news found.")
