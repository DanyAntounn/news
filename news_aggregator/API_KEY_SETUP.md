# 🔑 API KEY & EMAIL PASSWORD SETUP GUIDE

## Part 1: Get Your NewsAPI Key (Free)

### Step-by-Step with Screenshots

**Step 1**: Go to https://newsapi.org/

**Step 2**: Click the "Get API Key" button at the top

**Step 3**: Enter your email and password to create account

**Step 4**: Verify your email

**Step 5**: You'll see your API Key displayed

Example API Key:
```
abc1234def567ghijklmnopqr1234567
```

**Step 6**: Copy this entire string

**Step 7**: Open your `.env` file and paste it here:
```
NEWSAPI_KEY=abc1234def567ghijklmnopqr1234567
```

---

## Part 2: Create Gmail App Password (Free)

### ⚠️ IMPORTANT: These are NOT the Same

- **Your Gmail Password** = Used to log into Gmail
- **App Password** = A special password just for apps (what we need)

### Prerequisites

You MUST have 2-Step Verification enabled. If you don't:

1. Go to https://myaccount.google.com/
2. Click "Security" on the left sidebar
3. Scroll to "How you sign in to Google"
4. Click "2-Step Verification"
5. Follow the prompts to enable it
6. Use your phone number for verification

### Now Get Your App Password

1. Go to https://myaccount.google.com/apppasswords
2. You should see a dropdown for "Select the app and device you're using"
3. For **Select app**, choose: **Mail**
4. For **Select device**, choose: **Windows Computer**
5. Google will generate a 16-character password

Example:
```
abcd efgh ijkl mnop
```

6. Copy ONLY the letters and numbers (no spaces):
```
abcdefghijklmnop
```

7. Open your `.env` file and paste it here:
```
SENDER_PASSWORD=abcdefghijklmnop
```

⚠️ **Do NOT use spaces in the password!**

---

## Part 3: Complete Your .env File

Now that you have both keys, fill in this template:

```env
# Your NewsAPI key from Part 1
NEWSAPI_KEY=abc1234def567ghijklmnopqr1234567

# Your Gmail address
SENDER_EMAIL=youremail@gmail.com

# Your App Password from Part 2 (NO SPACES!)
SENDER_PASSWORD=abcdefghijklmnop

# Where to send emails (can be same as above)
RECIPIENT_EMAIL=youremail@gmail.com

# What time to send (24-hour format)
DAILY_HOUR=7
DAILY_MINUTE=0

# Today's topic
NEWS_TOPIC=Lebanon israel war
```

---

## Verification Checklist

After setup, verify:

- [ ] `.env` file exists in the `news_aggregator` folder
- [ ] NEWSAPI_KEY is filled in (34 characters)
- [ ] SENDER_PASSWORD is filled in (16 characters, no spaces)
- [ ] SENDER_EMAIL is your Gmail address
- [ ] DAILY_HOUR is a number 0-23
- [ ] Your .env file is saved

---

## Troubleshooting

### "Invalid API Key"
- Check you copied the key correctly from newsapi.org
- No extra spaces at the beginning or end
- Log in to newsapi.org and verify your key is active

### "Authentication Failed" (Email Error)
- ❌ Did you use your Gmail PASSWORD? 
  → Use APP PASSWORD instead!
- ❌ Did you include spaces in the app password?
  → Remove all spaces!
- ❌ Don't have 2-Step Verification?
  → Enable it first at https://myaccount.google.com/security
- ❌ Can't find "App passwords"?
  → You must enable 2-Step Verification first

### "Can't find app passwords page"
Go here directly: https://myaccount.google.com/apppasswords

If it says "This page isn't available", you need to:
1. Enable 2-Step Verification first
2. Wait 30 seconds
3. Try again

---

## Do NOT Share These!

- ⚠️ Never share your API Key
- ⚠️ Never share your App Password
- ⚠️ Never commit `.env` to GitHub
- ⚠️ Keep these private and secure!

---

## FAQs

**Q: Can I use my regular Gmail password?**
A: No! You must use an App Password. Gmail blocks regular passwords for security.

**Q: What if I lose my API Key?**
A: Log back into NewsAPI.org and regenerate it.

**Q: What if I lose my App Password?**
A: Go to https://myaccount.google.com/apppasswords and create a new one.

**Q: Do I pay for the free API?**
A: No! NewsAPI.org free tier includes 100 requests per day, which is plenty.

**Q: Can I use a different email provider (Outlook, Yahoo, etc.)?**
A: Yes, but the setup is different. You'll need your email provider's SMTP details.

---

**Once complete, you're ready to run the program!**
```powershell
python main.py
```
