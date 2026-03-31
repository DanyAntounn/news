# ⚡ QUICK START GUIDE

## 📋 Before You Begin - Checklist

- [ ] Get a free NewsAPI key from https://newsapi.org/
- [ ] Enable 2-Step Verification on your Gmail account
- [ ] Create a Gmail App Password
- [ ] Have your Gmail address ready
- [ ] Python 3.7+ is installed
- [ ] Internet connection is working

## 🚀 Setup in 5 Minutes

### 1️⃣ Create Configuration File

In the `news_aggregator` folder, create a new file called `.env` (just `.env`, not `.env.example`)

Copy this and fill in your information:

```
NEWSAPI_KEY=YOUR_API_KEY_HERE
SENDER_EMAIL=your.email@gmail.com
SENDER_PASSWORD=YOUR_APP_PASSWORD_HERE
RECIPIENT_EMAIL=your.email@gmail.com
DAILY_HOUR=7
DAILY_MINUTE=0
NEWS_TOPIC=Lebanon israel war
```

### 2️⃣ Get Your NewsAPI Key

1. Visit https://newsapi.org/
2. Sign up for free
3. Copy your API Key
4. Paste it into NEWSAPI_KEY in your .env file

### 3️⃣ Get Your Gmail App Password

1. Go to https://myaccount.google.com/
2. Click "Security" on the left
3. Enable "2-Step Verification" if not already enabled
4. Click "App passwords"
5. Select Mail + Windows Computer
6. Copy the generated password
7. Paste it into SENDER_PASSWORD in your .env file (remove spaces)

### 4️⃣ Install Dependencies

Open PowerShell in the `news_aggregator` folder and run:

```powershell
pip install -r requirements.txt
```

### 5️⃣ Run the Program

```powershell
python main.py
```

Choose option 2 to send a test email first!

## 🎯 How to Use

### From the Menu

```
1. Run scheduler → Daily emails at scheduled time
2. Send test digest → Send email immediately
3. Change topic → Update news topic anytime
4. View topic → See current topic
5. Test email → Verify Gmail setup
6. Test NewsAPI → Verify news API setup
0. Exit
```

### Example Usage

1. Run `python main.py`
2. Press `2` to send a test
3. Check your email
4. Press `3` to change topic (try "technology")
5. Press `2` again to test new topic
6. Press `1` to start daily scheduler
7. Press `Ctrl+C` to stop

## ✅ Verify Everything Works

After setup, test each component:

```powershell
# Test 1: Start the program
python main.py
# Choose option 6 to test NewsAPI

# Test 2: Test email
# Choose option 5 to test email

# Test 3: Send a test digest
# Choose option 2 to send immediately
# Check your inbox!
```

## 🔧 Common Issues

| Issue | Solution |
|-------|----------|
| Module not found | `pip install -r requirements.txt` |
| Email won't send | Check you used APP PASSWORD, not regular Gmail password |
| No articles found | Check NewsAPI key is correct |
| Can't find Python | Use full path: `C:\Users\User\Desktop\New folder\.venv\Scripts\python.exe` |

## 📧 Email Settings

- **Time**: Edit `DAILY_HOUR` and `DAILY_MINUTE` in `.env`
- **Topic**: Edit `NEWS_TOPIC` in `.env` or change from menu
- **Recipient**: Edit `RECIPIENT_EMAIL` in `.env`

## 📚 Popular Topics

```
"Lebanon israel war"
"technology news"
"artificial intelligence"
"sports"
"health"
"business"
"climate change"
"crypto"
```

## 🔄 Running Continuously

The scheduler will send emails daily at your set time, as long as:
- Terminal stays open
- Computer is ON (not in sleep)
- Internet is connected

To run 24/7, see SETUP_GUIDE.py for Task Scheduler setup.

## 📞 Need Help?

- NewsAPI: https://newsapi.org/docs
- Gmail App Passwords: https://support.google.com/accounts/answer/185833
- Python: https://python.org/docs/
- Schedule Package: https://schedule.readthedocs.io/

---

**You're all set! Run `python main.py` and enjoy your daily news digest! 📰**
