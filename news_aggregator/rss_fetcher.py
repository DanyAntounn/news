"""
Module to fetch news articles from RSS feeds
"""
import feedparser
from typing import List, Dict
from datetime import datetime


class RSSNewsFetcher:
    """Fetches news articles from RSS feeds"""
    
    # Major international news RSS feeds
    RSS_FEEDS = {
        'BBC': 'http://feeds.bbc.co.uk/news/rss.xml',
        'Reuters': 'https://www.reutersagency.com/feed/?taxonomy=best-topics&output=rss',
        'Guardian': 'https://www.theguardian.com/international/rss',
        'CNN': 'http://rss.cnn.com/rss/edition.rss',
        'Al Jazeera': 'https://www.aljazeera.com/xml/rss/all.xml',
        'France24': 'https://www.france24.com/en/rss',
        'DW': 'https://www.dw.com/en/rss',
        'AP News': 'https://apnews.com/hub/apf-wire',
        'Euronews': 'https://www.euronews.com/rss',
        'TRT': 'https://www.trtworld.com/feed/all'
    }
    
    def __init__(self):
        """Initialize RSS news fetcher"""
        pass
    
    def fetch_from_rss(self, feed_url: str, limit: int = 10) -> List[Dict]:
        """
        Fetch articles from a single RSS feed
        
        Args:
            feed_url: URL of the RSS feed
            limit: Maximum number of articles to fetch
        
        Returns:
            List of article dictionaries
        """
        try:
            feed = feedparser.parse(feed_url)
            articles = []
            
            if feed.bozo:
                print(f"Warning: Feed parsing issue: {feed.bozo_exception}")
            
            for entry in feed.entries[:limit]:
                articles.append({
                    'title': entry.get('title', 'N/A'),
                    'summary': entry.get('summary', entry.get('description', 'No summary available')),
                    'url': entry.get('link', '#'),
                    'source': feed.feed.get('title', 'Unknown'),
                    'published_at': entry.get('published', 'Unknown'),
                    'image': ''
                })
            
            return articles
        
        except Exception as e:
            print(f"Error fetching from RSS feed: {e}")
            return []
    
    def fetch_all_feeds(self, limit_per_feed: int = 5) -> List[Dict]:
        """
        Fetch articles from all major news feeds
        
        Args:
            limit_per_feed: Articles per feed
        
        Returns:
            Combined list of articles
        """
        all_articles = []
        
        for source_name, feed_url in self.RSS_FEEDS.items():
            print(f"Fetching from {source_name}...", end=" ")
            articles = self.fetch_from_rss(feed_url, limit_per_feed)
            all_articles.extend(articles)
            print(f"✓ ({len(articles)} articles)")
        
        return all_articles
    
    def search_articles(self, query: str, limit: int = 15) -> List[Dict]:
        """
        Fetch articles and filter by keyword
        
        Args:
            query: Search keyword (e.g., 'Lebanon', 'technology')
            limit: Maximum articles to return
        
        Returns:
            Filtered list of articles
        """
        all_articles = self.fetch_all_feeds(limit_per_feed=10)
        
        # Filter articles by keyword
        query_lower = query.lower()
        filtered = [
            article for article in all_articles
            if query_lower in article['title'].lower() or 
               query_lower in article['summary'].lower()
        ]
        
        return filtered[:limit]


if __name__ == '__main__':
    # Test the fetcher
    fetcher = RSSNewsFetcher()
    
    print("Fetching articles about 'technology'...\n")
    articles = fetcher.search_articles('technology', limit=5)
    
    print(f"\nFound {len(articles)} articles:")
    for article in articles:
        print(f"\n- {article['title']}")
        print(f"  Source: {article['source']}")
        print(f"  URL: {article['url']}")
        print(f"  Summary: {article['summary'][:100]}...")
