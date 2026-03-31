# 🚀 GitHub Actions Setup Guide

## How it Works

GitHub Actions is a **completely free** automation platform that:
- ✅ Runs your code on a schedule (daily, weekly, etc.)
- ✅ Launches automatically without keeping your PC on
- ✅ Handles secrets securely (API keys, passwords)
- ✅ Keeps logs of each run
- ✅ No credit card required

## Setup Steps

### Step 1: Create a GitHub Account

1. Go to https://github.com/
2. Sign up if you don't have an account (free)
3. Verify your email

### Step 2: Create a New Repository

1. Click the **+** icon in top right → "New repository"
2. Name it: `news-aggregator`
3. Choose **Public** (required for free GitHub Actions)
4. Click "Create repository"

### Step 3: Push Your Code to GitHub

Open PowerShell in your `news_aggregator` folder and run:

```powershell
# Initialize git (if not already done)
git init
git config user.name "Your Name"
git config user.email "your.email@gmail.com"

# Add all files
git add .

# Create first commit
git commit -m "Initial news aggregator setup"

# Add remote repository (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/news-aggregator.git

# Push to GitHub (you'll be asked for credentials)
git branch -M main
git push -u origin main
```

If prompted for credentials:
- **Username**: Your GitHub username
- **Password**: Create a Personal Access Token (see below)

### Creating a GitHub Personal Access Token (if needed)

1. Go to https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Give it the name: `news-aggregator`
4. Check these scopes:
   - `repo` (full control of private repositories)
   - `workflow` (update GitHub Action workflows)
5. Click "Generate token"
6. **Copy the token** (you won't see it again!)
7. Use this as your password when pushing

### Step 4: Add GitHub Secrets

Your API keys and passwords need to be stored securely as "Secrets":

1. Go to your GitHub repository
2. Click **Settings** (top menu)
3. Click **Secrets and variables** → **Actions** (left sidebar)
4. Click **"New repository secret"** and add these:

| Secret Name | Value |
|---|---|
| `NEWSAPI_KEY` | Your NewsAPI key |
| `SENDER_EMAIL` | antoundany4@gmail.com |
| `SENDER_PASSWORD` | Your Gmail app password |
| `RECIPIENT_EMAIL` | antoundany4@gmail.com |
| `NEWS_TOPIC` | Lebanon israel war |

**Important**: Each secret is encrypted and never shown in logs!

### Step 5: Enable GitHub Actions

1. Click the **Actions** tab in your repository
2. You should see "Daily News Digest" workflow
3. Click it and verify it's enabled (green checkmark)

### Step 6: Adjust the Schedule (Optional)

The workflow runs daily at **7:00 AM UTC**. To change it:

1. Edit `.github/workflows/daily_news.yml`
2. Find this line:
   ```yaml
   - cron: '0 7 * * *'
   ```
3. Use [cron format](https://crontab.guru/):
   - `0 7 * * *` = 7:00 AM every day
   - `0 14 * * *` = 2:00 PM every day
   - `0 7 * * 1` = 7:00 AM every Monday
   - `*/4 * * * *` = Every 4 hours

4. Save and push the changes:
   ```powershell
   git add .github/workflows/daily_news.yml
   git commit -m "Update schedule time"
   git push
   ```

### Step 7: Test It

1. Go to **Actions** tab in GitHub
2. Click **"Daily News Digest"** workflow
3. Click **Run workflow** → **Run workflow** (green button)
4. Wait 2-3 minutes
5. You should get an email! ✉️

## 📊 Viewing Logs

After the workflow runs:

1. Click **Actions** tab
2. Click the latest workflow run
3. Click **send-news-digest** to see details
4. Read the logs to see what happened

## 🔄 Automatic Runs

The workflow will run automatically at your scheduled time **every single day**, 24/7, even when your computer is off!

## ⏰ Time Zone Note

The `cron` schedule uses **UTC time**. Convert your local time:
- EST (UTC-5): Subtract 5 hours → For 7 AM EST, use `0 12 * * *`
- PST (UTC-8): Subtract 8 hours → For 7 AM PST, use `0 15 * * *`
- UK (UTC+0): Same as UTC
- UAE (UTC+4): Subtract 4 hours → For 7 AM, use `0 3 * * *`

## 🔐 Security Notes

- ✅ Never put secrets in `.env` file in GitHub
- ✅ Use GitHub Secrets for sensitive data
- ✅ Logs show output but never expose secret values
- ✅ Personal Access Token can be revoked anytime

## 📝 Environment Variables

To add more configuration, edit the **Secrets** in GitHub:

1. Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Reference it in the workflow with `${{ secrets.YOUR_SECRET_NAME }}`

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Repository not found" | Make sure repository is PUBLIC and you used correct name |
| Email not received | Check workflow logs in Actions tab, verify secrets are correct |
| Workflow won't run | Enable GitHub Actions in Settings → Actions → Allow all actions |
| "Permission denied" | Create a new Personal Access Token with correct scopes |

## 📚 Learn More

- GitHub Actions Docs: https://docs.github.com/en/actions
- Cron Schedule Helper: https://crontab.guru/
- Python in GitHub Actions: https://github.com/actions/setup-python

---

**That's it! Your news aggregator now runs automatically in the cloud! 🎉**

Check your email at the scheduled time to see your daily digest arrive automatically.
