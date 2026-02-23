# translation-gateway
Created by RepoPatchBot pipeline

## Local Run Instructions
To run the translation gateway locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd translation-gateway
   ```

2. **Install dependencies**:
   Make sure you have Python 3.10+ installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Store your secrets in environment variables:
   ```bash
   export OPENROUTER_API_KEY=<your_openrouter_api_key>
   export TELEGRAM_BOT_TOKEN=<your_telegram_bot_token>
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

## Telegram Webhook Setup
To set up the Telegram webhook for your bot:

1. **Create a new bot** using [@BotFather](https://t.me/botfather) on Telegram and obtain your bot token.

2. **Set the webhook URL**:
   Use the following command to set your webhook URL (replace `<your_webhook_url>` with your actual URL):
   ```bash
   curl -X POST https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/setWebhook -d "url=<your_webhook_url>"
   ```

3. **Verify the webhook**:
   Ensure that your webhook is set correctly by checking the response from the above command.

Now your bot should be ready to receive messages via the webhook!