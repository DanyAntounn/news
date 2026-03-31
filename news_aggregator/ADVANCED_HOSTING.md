# ☁️ Alternative Free Hosting: AWS Lambda & Google Cloud

## If You Want to Use AWS Lambda

### Step 1: Create AWS Account
1. Go to https://aws.amazon.com
2. Click "Create an AWS Account"
3. Verify with credit card (required for free tier, but you won't be charged)
4. Complete sign-up

### Step 2: Create Lambda Function
1. Go to AWS Lambda console
2. Click "Create function"
3. Name: `news-aggregator`
4. Runtime: Python 3.11
5. Click "Create function"

### Step 3: Upload Code
1. Zip your `news_aggregator` folder (excluding `.env`)
2. In Lambda, click Upload from .zip file
3. Upload the zip
4. Set Handler to: `lambda_function.lambda_handler`

### Step 4: Create Lambda Handler
Create a file called `lambda_function.py` in your project:

```python
import sys
sys.path.insert(0, '/var/task')

from news_fetcher import NewsFetcher
from email_sender import EmailSender
import os

def lambda_handler(event, context):
    try:
        # Fetch articles
        fetcher = NewsFetcher()
        articles = fetcher.fetch_articles(query='Lebanon israel war', page_size=15)
        
        # Send email
        mailer = EmailSender()
        mailer.send_email(
            recipient_email=os.environ['RECIPIENT_EMAIL'],
            articles=articles,
            topic='Lebanon israel war'
        )
        
        return {'statusCode': 200, 'body': 'Email sent successfully'}
    except Exception as e:
        return {'statusCode': 500, 'body': str(e)}
```

### Step 5: Set Environment Variables
1. In Lambda console, scroll to "Environment variables"
2. Add:
   - `NEWSAPI_KEY` = your key
   - `SENDER_EMAIL` = your email
   - `SENDER_PASSWORD` = app password
   - `RECIPIENT_EMAIL` = recipient
   - `NEWS_TOPIC` = topic

### Step 6: Increase Timeout
1. Scroll to "General configuration"
2. Click "Edit"
3. Set Timeout to: 60 seconds
4. Save

### Step 7: Create CloudWatch Rule
1. Go to CloudWatch console
2. Click "Rules" in left sidebar
3. Click "Create rule"
4. Schedule expression: `cron(0 7 * * ? *)`
5. Target: Lambda function
6. Select your `news-aggregator` function
7. Click "Create rule"

### Cost
- 1,000,000 free invocations per month
- Your usage: ~30/month = FREE

### Difficulty: Medium

---

## If You Want to Use Google Cloud Functions

### Step 1: Create Google Cloud Account
1. Go to https://cloud.google.com/free
2. Click "Start free"
3. Login with Google account
4. Add credit card (required but won't be charged for free tier)
5. Complete setup

### Step 2: Create Cloud Function
1. Go to Cloud Functions console
2. Click "Create Function"
3. Name: `news-aggregator`
4. Runtime: Python 3.11
5. Entry point: `send_digest`
6. Click "Create"

### Step 3: Add Code
In the inline editor, paste:

```python
import functions_framework
from news_fetcher import NewsFetcher
from email_sender import EmailSender
import os

@functions_framework.http
def send_digest(request):
    try:
        fetcher = NewsFetcher()
        articles = fetcher.fetch_articles(
            query='Lebanon israel war',
            page_size=15
        )
        
        mailer = EmailSender()
        mailer.send_email(
            recipient_email=os.environ['RECIPIENT_EMAIL'],
            articles=articles,
            topic='Lebanon israel war'
        )
        
        return 'Email sent successfully', 200
    except Exception as e:
        return str(e), 500
```

### Step 4: Set Environment Variables
1. Scroll to "Runtime settings"
2. Click "Edit"
3. Under "Environment variables" add:
   - `NEWSAPI_KEY` = your key
   - `SENDER_EMAIL` = your email
   - `SENDER_PASSWORD` = app password
   - `RECIPIENT_EMAIL` = recipient
   - `NEWS_TOPIC` = topic

### Step 5: Increase Timeout
1. In "Runtime settings", set Timeout: 60 seconds

### Step 6: Create Cloud Scheduler Task
1. Go to Cloud Scheduler
2. Click "Create Job"
3. Name: `news-aggregator-daily`
4. Frequency: `0 7 * * *` (7 AM every day)
5. Timezone: Select your timezone
6. Execution type: HTTP
7. URL: Copy the function URL from Cloud Functions
8. HTTP method: GET
9. Click "Create"

### Cost
- 2,000,000 free invocations per month
- Your usage: ~30/month = FREE

### Difficulty: Medium

---

## Quick Comparison

| Feature | GitHub Actions | AWS Lambda | Google Cloud |
|---------|---|---|---|
| Setup Time | 15 min | 30 min | 25 min |
| Monthly Cost | $0 | $0 | $0 |
| Free Invocations | Unlimited | 1M | 2M |
| Ease of Use | Easy | Medium | Medium |
| **Recommended** | ✅ YES | ⭐ | ⭐ |

---

## My Recommendation

**Start with GitHub Actions** (in GITHUB_ACTIONS_SETUP.md)
- Easiest to set up
- No additional accounts needed
- Perfect for your use case

**If you want backup/redundancy**, add Google Cloud later
- Free tier can handle it
- More professional monitoring

**Skip AWS Lambda for now**
- More complex
- Similar pricing to Google Cloud
- GitHub Actions is better for scheduled tasks

---

## Questions?

For platform-specific help:
- **GitHub Actions**: https://docs.github.com/en/actions
- **AWS Lambda**: https://aws.amazon.com/lambda/
- **Google Cloud**: https://cloud.google.com/functions/

Good luck! 🚀
