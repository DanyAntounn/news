"""
Module to schedule daily news digest emails
"""
import schedule
import time
import os
from dotenv import load_dotenv
from news_fetcher import NewsFetcher
from email_sender import EmailSender
from datetime import datetime


class NewsScheduler:
    """Schedules and runs daily news digest tasks"""
    
    def __init__(self):
        """Initialize scheduler with configuration from .env"""
        load_dotenv()
        
        # Load configuration
        self.news_topic = os.getenv('NEWS_TOPIC', 'world news')
        self.daily_hour = int(os.getenv('DAILY_HOUR', '7'))
        self.daily_minute = int(os.getenv('DAILY_MINUTE', '0'))
        self.recipient_email = os.getenv('RECIPIENT_EMAIL')
        
        # Initialize components
        self.fetcher = NewsFetcher()
        self.mailer = EmailSender()
        
        self.is_running = False
    
    def send_digest(self):
        """Fetch articles and send email"""
        print(f"\n{'='*60}")
        print(f"Fetching articles for: {self.news_topic}")
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}")
        
        try:
            # Fetch articles
            articles = self.fetcher.fetch_articles(
                query=self.news_topic,
                page_size=15
            )
            
            if not articles:
                print("⚠ No articles found for the given topic.")
            else:
                print(f"✓ Found {len(articles)} articles")
            
            # Send email
            success = self.mailer.send_email(
                recipient_email=self.recipient_email,
                articles=articles,
                topic=self.news_topic
            )
            
            if success:
                print("✓ Daily digest completed successfully!")
            else:
                print("✗ Failed to send email")
        
        except Exception as e:
            print(f"✗ Error in send_digest: {e}")
    
    def schedule_daily(self):
        """Schedule the digest to run daily at specified time"""
        time_str = f"{self.daily_hour:02d}:{self.daily_minute:02d}"
        schedule.every().day.at(time_str).do(self.send_digest)
        print(f"✓ Scheduled daily digest at {time_str}")
    
    def run(self, test_mode: bool = False):
        """
        Run the scheduler
        
        Args:
            test_mode: If True, run once immediately and exit
        """
        self.is_running = True
        self.schedule_daily()
        
        if test_mode:
            print("\n⚡ TEST MODE: Running digest once...")
            self.send_digest()
            return
        
        print("\n✓ Scheduler running. Press Ctrl+C to stop.")
        print("Waiting for scheduled time...\n")
        
        try:
            while self.is_running:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
        except KeyboardInterrupt:
            print("\n\nScheduler stopped by user.")
            self.is_running = False
    
    def change_topic(self, new_topic: str):
        """Change the news topic dynamically"""
        self.news_topic = new_topic
        print(f"✓ Topic changed to: {new_topic}")
    
    def stop(self):
        """Stop the scheduler"""
        self.is_running = False
        print("Scheduler stopped.")


if __name__ == '__main__':
    scheduler = NewsScheduler()
    
    # Run in production mode
    scheduler.run(test_mode=False)
