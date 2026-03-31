"""
SETUP GUIDE - Step by Step Instructions
========================================
"""

# ============================================================================
# STEP 1: Get Your NewsAPI Key
# ============================================================================

"""
1. Go to https://newsapi.org/
2. Click "Get API Key" in the top right
3. Create a free account
4. You'll receive an API Key (looks like: abc123xyz789...)
5. Copy this key for later
"""

# ============================================================================
# STEP 2: Create Gmail App Password
# ============================================================================

"""
IMPORTANT: You must have 2-Step Verification enabled on your Gmail first!

1. Go to https://myaccount.google.com/security
2. Click on "2-Step Verification" and set it up (if not already done)
3. Once 2FA is enabled, go to https://myaccount.google.com/apppasswords
4. Select:
   Device: Windows Computer
   App: Mail
5. Google will generate a 16-character password
6. Copy this password (it should look like: xxxx xxxx xxxx xxxx)
   ** Use only the letters and numbers, no spaces **
"""

# ============================================================================
# STEP 3: Create .env File
# ============================================================================

"""
1. In the news_aggregator folder, create a new file named: .env
   (NOT .env.example, but .env)

2. Copy and paste this into the .env file:

NEWSAPI_KEY=paste_your_newsapi_key_here
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=paste_your_16_char_app_password_here
RECIPIENT_EMAIL=your_email@gmail.com
DAILY_HOUR=7
DAILY_MINUTE=0
NEWS_TOPIC=Lebanon israel war

3. Replace the values:
   - NEWSAPI_KEY: Your API key from Step 1
   - SENDER_EMAIL: Your Gmail address
   - SENDER_PASSWORD: Your app password from Step 2 (without spaces)
   - RECIPIENT_EMAIL: Email to receive the digests (can be same as sender)
   - DAILY_HOUR: What hour to send (0-23, so 7 = 7 AM)
   - DAILY_MINUTE: What minute (0-59)
   - NEWS_TOPIC: What news to search for
"""

# ============================================================================
# STEP 4: Test Installation
# ============================================================================

"""
Open PowerShell in the news_aggregator folder and run:

python main.py

Select option 5 to test email connection
Select option 6 to test NewsAPI connection
"""

# ============================================================================
# STEP 5: Send First Test Digest
# ============================================================================

"""
From the menu:
- Select option 2 to send a test digest immediately
- Check your inbox for the email
"""

# ============================================================================
# STEP 6: Run the Scheduler
# ============================================================================

"""
To start sending daily digests at your scheduled time:
- From the menu, select option 1
- The program will run continuously
- Keep the terminal open
- Press Ctrl+C to stop

To run in the background permanently, see ADVANCED section below.
"""

# ============================================================================
# ADVANCED: Run continuously on Windows
# ============================================================================

"""
To keep the news aggregator running 24/7:

Option A: Use Windows Task Scheduler
1. Open Windows Task Scheduler (Windows + R, type "taskschd.msc")
2. Right-click "Task Scheduler Library" → Create Task
3. Name it "News Aggregator"
4. Go to "Triggers" tab → New Trigger
5. Set to run daily at your preferred time (e.g., 7:00 AM)
6. Go to "Actions" tab → New Action
7. Set Action to "Start a program"
8. Program: C:/Users/User/Desktop/New folder/.venv/Scripts/python.exe
   (adjust path based on your actual location)
9. Arguments: scheduler.py
10. Start in: C:/Users/User/Desktop/New folder/news_aggregator
11. Enable "Run with highest privileges"
12. Click OK

Option B: Use a batch file to run at startup
1. Create a file named "run_news_aggregator.bat":

    @echo off
    cd C:\Users\User\Desktop\New folder\news_aggregator
    C:\Users\User\Desktop\New folder\.venv\Scripts\python.exe scheduler.py

2. Save this file
3. Copy the shortcut to: C:\Users\User\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
4. Now it will run automatically when you start Windows

Option C: Use WSL or a VPS for 24/7 operation
- If you want it running even when your computer is off, 
  deploy to a cloud service or always-on server
"""

# ============================================================================
# TROUBLESHOOTING
# ============================================================================

"""
PROBLEM: "Module not found" or "No module named..."
SOLUTION: Make sure you're in the correct folder and ran:
         pip install -r requirements.txt

PROBLEM: "Authentication failed" or Email won't send
SOLUTION: 
  - Did you create a Gmail APP PASSWORD (not your regular password)?
  - Is 2-Step Verification enabled on your Gmail?
  - No spaces in your app password in .env file

PROBLEM: "Invalid API key" or No articles found
SOLUTION: Check your NEWSAPI_KEY in .env file
         Visit https://newsapi.org/account to verify

PROBLEM: Python is not recognized as a command
SOLUTION: In PowerShell, use the full path:
         C:\Users\User\Desktop\New folder\.venv\Scripts\python.exe main.py

PROBLEM: Scheduler starts but doesn't run at time
SOLUTION: 
  - Check your DAILY_HOUR and DAILY_MINUTE settings (use 24-hour format)
  - Your computer must be on and not in sleep mode
  - Keep the terminal open
"""

# ============================================================================
# CHANGING YOUR NEWS TOPIC
# ============================================================================

"""
During runtime:
1. From the menu, select option 3
2. Type your new topic (examples: 'technology', 'sports', 'AI')

Or edit it directly:
1. Open the .env file
2. Change NEWS_TOPIC to your desired topic
3. Save the file
4. Restart the program
"""

# ============================================================================
# SAMPLE TOPICS TO TRY
# ============================================================================

SAMPLE_TOPICS = [
    "Lebanon israel war",
    "artificial intelligence",
    "technology",
    "cryptocurrency",
    "climate change",
    "sports",
    "health",
    "business",
    "space exploration",
    "science",
    "politics",
    "economy"
]

# ============================================================================
# GETTING HELP
# ============================================================================

"""
NewsAPI Documentation: https://newsapi.org/docs
Gmail App Passwords Help: https://support.google.com/accounts/answer/185833
Python Documentation: https://python.org/docs/
Schedule Library: https://schedule.readthedocs.io/
"""
