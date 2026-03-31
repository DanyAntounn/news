# Daily News Aggregator AI

An AI-powered news aggregator that fetches articles from multiple sources, filters by topic, and sends them via email on a schedule.

## Features

✨ **Smart Article Fetching** - Fetches news from global news sources
📧 **Automated Email Delivery** - Sends formatted digests to your inbox
🎯 **Dynamic Topic Filtering** - Change topics anytime
⏰ **Scheduled Delivery** - Daily delivery at your preferred time
🌍 **Multi-Source Support** - Aggregates from major news outlets
📱 **Beautiful Email Formatting** - Professional HTML emails

## Supported News Sources

The system fetches from major international news outlets including:
- BBC News
- The Guardian
- New York Times
- Reuters
- The Atlantic
- Forbes
- France24
- CNN
- Wall Street Journal
- Haaretz
- Al Arabiya
- Al Hadath
- Gulf Times
- Asharq Al-Awsat
- Al Dustour
- Annahar
- L'Orient-Le Jour

## Setup Instructions

### 1. Prerequisites

- Python 3.7 or higher
- Gmail account with 2FA enabled

### 2. Installation

```bash
# Navigate to the project folder
cd news_aggregator

# Install dependencies
pip install -r requirements.txt
```

### 3. Get a NewsAPI Key

1. Visit [NewsAPI.org](https://newsapi.org/)
2. Sign up for a free account
3. Copy your API key

### 4. Create Gmail App Password

1. Go to [Google Account Settings](https://myaccount.google.com/)
2. Enable 2-Step Verification (if not already enabled)
3. Go to App passwords (under Security)
4. Select "Mail" and "Windows Computer"
5. Copy the generated password

### 5. Configure Environment

1. Rename `.env.example` to `.env`
2. Fill in your credentials:

```env
NEWSAPI_KEY=your_newsapi_key_here
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_gmail_app_password_here
RECIPIENT_EMAIL=recipient@example.com
DAILY_HOUR=7
DAILY_MINUTE=0
NEWS_TOPIC=Lebanon israel war
```

## Usage

### Run the Interactive Menu

```bash
python main.py
```

### Run the Scheduler (Background Mode)

```bash
python scheduler.py
```

Press `Ctrl+C` to stop the scheduler.

### Command Line Options

From the interactive menu:
- **Option 1**: Start the scheduler for daily automatic emails
- **Option 2**: Send a test digest immediately
- **Option 3**: Change the news topic
- **Option 4**: View current topic
- **Option 5**: Test email connection
- **Option 6**: Test NewsAPI connection

## Configuration

Edit `.env` to customize:

- `NEWSAPI_KEY`: Your NewsAPI key
- `SENDER_EMAIL`: Your Gmail address
- `SENDER_PASSWORD`: Gmail app password
- `RECIPIENT_EMAIL`: Where to send digests
- `DAILY_HOUR`: Hour for daily delivery (0-23)
- `DAILY_MINUTE`: Minute for daily delivery (0-59)
- `NEWS_TOPIC`: Topic to search (e.g., "Lebanon israel war", "technology", "sports")

## How It Works

1. **Fetcher** (`news_fetcher.py`): Queries NewsAPI for articles matching your topic
2. **Processor**: Extracts title, summary, and URL from articles
3. **Formatter**: Creates a beautiful HTML email with all articles
4. **Scheduler** (`scheduler.py`): Runs daily at your specified time
5. **Mailer** (`email_sender.py`): Sends the formatted email via Gmail

## Example Workflow

1. Run the program: `python main.py`
2. Choose option 2 to test immediately
3. Check your email for the formatted digest
4. Change the topic if desired (option 3)
5. Start the scheduler (option 1) for daily delivery

## Topic Examples

Some popular topics to try:
- `lebanon israel war`
- `artificial intelligence`
- `technology startup`
- `climate change`
- `cryptocurrency`
- `sports`
- `health`

## Troubleshooting

### Email Not Sending
- Verify your app password is correct (not your Gmail password)
- Check that 2FA is enabled on your Google Account
- Less secure apps might need to be allowed

### No Articles Found
- Check your internet connection
- Verify your NewsAPI key is valid
- Try a different topic

### Scheduler Not Running
- Make sure the terminal stays open
- Check system time matches your DAILY_HOUR setting
- Verify Python is running in the right directory

## Advanced Usage

### Fetching from Specific Sources

Open `news_fetcher.py` and modify the `fetch_from_sources()` method with source codes:

```python
articles = fetcher.fetch_from_sources(['bbc-news', 'cnn', 'the-guardian-uk'])
```

### Filtering Articles

Enhance the fetching logic to filter by:
- Language
- Publication date
- Article length
- Popularity

### Integration Ideas

- Connect to a database to store articles
- Add sentiment analysis
- Create a web dashboard
- Build a Telegram/Discord bot
- Add multiple topic subscriptions

## Limitations

- Free NewsAPI limited to 100 requests per day
- Some news sources may not be available in the free tier
- Article summaries come from the source, not AI-generated

## License

This project is provided as-is for personal use.

## Support

For issues with:
- **NewsAPI**: Visit https://newsapi.org/docs
- **Gmail**: Check https://support.google.com/
- **Python**: Refer to Python documentation

---

Happy reading! 📰
