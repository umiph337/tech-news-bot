# 🌤️ Weather News Bot 📩

This is a Python-based Telegram bot that **automatically fetches and summarizes daily weather news** from VNExpress and sends it to your Telegram account.

## 🚀 Features
- ✅ Fetches **latest weather news** from VNExpress RSS feed
- ✅ Summarizes the news using **rule-based extraction**
- ✅ Sends updates **daily to Telegram**
- ✅ Automated using **GitHub Actions**

## 📌 How It Works
1. GitHub Actions **runs the script daily** (8:00 AM Vietnam time)
2. The script **fetches weather news** from VNExpress
3. It **summarizes the first sentence** of each article
4. The bot **sends the summary to Telegram**

## 🛠️ Setup Instructions
### 1️⃣ Create a Telegram Bot
1. Open Telegram and search for `BotFather`
2. Type `/newbot` and follow instructions
3. Get the **Bot Token**

### 2️⃣ Get Your Telegram Chat ID
1. Open [@userinfobot](https://t.me/useridinfobot)
2. Send `/start` and get your **Chat ID**

### 3️⃣ Store API Keys in GitHub Secrets
1. Go to **GitHub Repository → Settings → Secrets → Actions**
2. Add:
   - `TELEGRAM_BOT_TOKEN`: Your bot token
   - `TELEGRAM_CHAT_ID`: Your chat ID

### 4️⃣ Enable GitHub Actions
1. Go to `.github/workflows/weather_bot.yml`
2. GitHub will **run the script daily automatically**

## 🏃‍♂️ Run Manually (Optional)
To run manually, go to the **"Actions" tab in GitHub** and trigger the workflow.

## 🔥 Future Improvements
- Add **AI summarization (BART, T5)**
- Send news via **Email**
- Support **multiple sources**

---

📬 **Created with ❤️ by [Your Name]**
