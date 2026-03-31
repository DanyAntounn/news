"""
Module to fetch news articles from NewsAPI
"""
import requests
from typing import List, Dict
import os
from dotenv import load_dotenv


class NewsFetcher:
    """Fetches news articles from NewsAPI based on search queries"""
    
    def __init__(self, api_key: str = None):
        """
        Initialize NewsAPI fetcher
        
        Args:
            api_key: NewsAPI key (if None, reads from environment)
        """
        load_dotenv()
        self.api_key = api_key or os.getenv('NEWSAPI_KEY')
        self.base_url = 'https://newsapi.org/v2/everything'
        
        if not self.api_key:
            raise ValueError("NEWSAPI_KEY not found in environment variables")
    
    def fetch_articles(self, query: str, language: str = 'en', 
                      sort_by: str = 'publishedAt', page_size: int = 10) -> List[Dict]:
        """
        Fetch articles from NewsAPI
        
        Args:
            query: Search query (topic)
            language: Language code (default: 'en')
            sort_by: Sort order ('publishedAt', 'relevancy', 'popularity')
            page_size: Number of articles to fetch (max 100)
        
        Returns:
            List of article dictionaries
        """
        try:
            params = {
                'q': query,
                'language': language,
                'sortBy': sort_by,
                'pageSize': page_size,
                'apiKey': self.api_key
            }
            
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('status') != 'ok':
                print(f"API Error: {data.get('message', 'Unknown error')}")
                return []
            
            articles = []
            for article in data.get('articles', []):
                articles.append({
                    'title': article.get('title', 'N/A'),
                    'summary': article.get('description', 'No summary available'),
                    'url': article.get('url', '#'),
                    'source': article.get('source', {}).get('name', 'Unknown'),
                    'published_at': article.get('publishedAt', 'Unknown'),
                    'image': article.get('urlToImage', '')
                })
            
            return articles
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching articles: {e}")
            return []
    
    def fetch_from_sources(self, sources: List[str], query: str = None) -> List[Dict]:
        """
        Fetch articles from specific sources
        
        Args:
            sources: List of source identifiers (BBC, guardian, etc.)
            query: Optional search query
        
        Returns:
            List of article dictionaries
        """
        try:
            url = 'https://newsapi.org/v2/top-headlines'
            
            params = {
                'sources': ','.join(sources),
                'pageSize': 10,
                'apiKey': self.api_key
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('status') != 'ok':
                print(f"API Error: {data.get('message', 'Unknown error')}")
                return []
            
            articles = []
            for article in data.get('articles', []):
                articles.append({
                    'title': article.get('title', 'N/A'),
                    'summary': article.get('description', 'No summary available'),
                    'url': article.get('url', '#'),
                    'source': article.get('source', {}).get('name', 'Unknown'),
                    'published_at': article.get('publishedAt', 'Unknown'),
                    'image': article.get('urlToImage', '')
                })
            
            return articles
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching from sources: {e}")
            return []


if __name__ == '__main__':
    # Test the fetcher
    fetcher = NewsFetcher()
    articles = fetcher.fetch_articles('technology', page_size=5)
    
    print(f"Found {len(articles)} articles:")
    for article in articles:
        print(f"\n- {article['title']}")
        print(f"  URL: {article['url']}")
        print(f"  Summary: {article['summary'][:100]}...")
