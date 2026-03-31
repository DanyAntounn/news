"""
Main entry point for News Aggregator AI
Provides CLI interface to manage and run the news scheduler
"""
import sys
import os
from dotenv import load_dotenv
from scheduler import NewsScheduler
from news_fetcher import NewsFetcher
from email_sender import EmailSender


def display_menu():
    """Display main menu"""
    print("\n" + "="*60)
    print("📰 DAILY NEWS AGGREGATOR")
    print("="*60)
    print("\n1. Run scheduler (daily delivery)")
    print("2. Send test digest now")
    print("3. Change topic")
    print("4. View current topic")
    print("5. Test email connection")
    print("6. View NewsAPI status")
    print("0. Exit")
    print("\n" + "-"*60)


def main():
    """Main application loop"""
    load_dotenv()
    
    scheduler = NewsScheduler()
    
    print("\n" + "="*60)
    print("🚀 INITIALIZING NEWS AGGREGATOR")
    print("="*60)
    print(f"\n✓ Sender Email: {scheduler.mailer.sender_email}")
    print(f"✓ Recipient Email: {scheduler.recipient_email}")
    print(f"✓ Current Topic: {scheduler.news_topic}")
    print(f"✓ Scheduled Time: {scheduler.daily_hour:02d}:{scheduler.daily_minute:02d}")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (0-6): ").strip()
        
        if choice == '1':
            # Run scheduler
            print("\n⏰ Starting scheduler...")
            try:
                scheduler.run(test_mode=False)
            except KeyboardInterrupt:
                print("\n✓ Scheduler stopped.")
        
        elif choice == '2':
            # Send test digest
            print("\n⚡ Sending test digest...")
            scheduler.send_digest()
        
        elif choice == '3':
            # Change topic
            new_topic = input("\nEnter new topic (e.g., 'Lebanon israel war', 'technology', 'sports'): ").strip()
            if new_topic:
                scheduler.change_topic(new_topic)
        
        elif choice == '4':
            # View current topic
            print(f"\nCurrent topic: {scheduler.news_topic}")
        
        elif choice == '5':
            # Test email connection
            print("\n🔐 Testing email connection...")
            try:
                mailer = EmailSender()
                print("✓ Email credentials loaded successfully")
                
                test_email = input("Enter email to test (or press Enter to skip): ").strip()
                if test_email:
                    test_articles = [{
                        'title': 'Test Article',
                        'summary': 'This is a test email from your News Aggregator.',
                        'url': 'https://example.com',
                        'source': 'Test',
                        'published_at': 'Just now'
                    }]
                    mailer.send_email(test_email, test_articles, 'Test')
            except Exception as e:
                print(f"✗ Error: {e}")
        
        elif choice == '6':
            # Test NewsAPI
            print("\n🔍 Testing NewsAPI connection...")
            try:
                fetcher = NewsFetcher()
                articles = fetcher.fetch_articles('test', page_size=1)
                if articles:
                    print(f"✓ NewsAPI is working!")
                    print(f"  Sample article: {articles[0]['title'][:50]}...")
                else:
                    print("✗ Could not fetch articles")
            except Exception as e:
                print(f"✗ Error: {e}")
        
        elif choice == '0':
            # Exit
            print("\n👋 Goodbye!")
            sys.exit(0)
        
        else:
            print("\n✗ Invalid choice. Please try again.")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"\n✗ Fatal error: {e}")
        sys.exit(1)
