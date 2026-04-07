"""
Module to fetch news articles from RSS feeds
"""
import feedparser
import re
from typing import List, Dict
from datetime import datetime, timedelta
import time


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

    # Common country names (lowercase). Used to detect country-related conflict news.
    COMMON_COUNTRIES = [
        "afghanistan","albania","algeria","andorra","angola","antigua and barbuda",
        "argentina","armenia","australia","austria","azerbaijan","bahamas","bahrain",
        "bangladesh","barbados","belarus","belgium","belize","benin","bhutan","bolivia",
        "bosnia and herzegovina","botswana","brazil","brunei","bulgaria","burkina faso",
        "burundi","cambodia","cameroon","canada","cape verde","central african republic",
        "chad","chile","china","colombia","comoros","congo","costa rica","cote d'ivoire",
        "croatia","cuba","cyprus","czechia","czech republic","denmark","djibouti","dominica",
        "dominican republic","ecuador","egypt","el salvador","equatorial guinea","eritrea",
        "estonia","eswatini","ethiopia","fiji","finland","france","gabon","gambia","georgia",
        "germany","ghana","greece","grenada","guatemala","guinea","guinea-bissau","guyana",
        "haiti","honduras","hungary","iceland","india","indonesia","iran","iraq","ireland",
        "israel","italy","jamaica","japan","jordan","kazakhstan","kenya","kiribati","kuwait",
        "kyrgyzstan","laos","latvia","lebanon","lesotho","liberia","libya","liechtenstein",
        "lithuania","luxembourg","madagascar","malawi","malaysia","maldives","mali","malta",
        "marshall islands","mauritania","mauritius","mexico","micronesia","moldova","monaco",
        "mongolia","montenegro","morocco","mozambique","myanmar","namibia","nauru","nepal",
        "netherlands","new zealand","nicaragua","niger","nigeria","north korea","north macedonia",
        "norway","oman","pakistan","palau","panama","papua new guinea","paraguay","peru",
        "philippines","poland","portugal","qatar","romania","russia","russian federation",
        "rwanda","saint kitts and nevis","saint lucia","saint vincent and the grenadines",
        "samoa","san marino","sao tome and principe","saudi arabia","senegal","serbia",
        "seychelles","sierra leone","singapore","slovakia","slovenia","solomon islands",
        "somalia","south africa","south korea","south sudan","spain","sri lanka","sudan",
        "suriname","sweden","switzerland","syria","taiwan","tajikistan","tanzania","thailand",
        "timor-leste","togo","tonga","trinidad and tobago","tunisia","turkey","turkmenistan",
        "tuvalu","uganda","ukraine","united arab emirates","united kingdom","uk",
        "united states","usa","u s","uruguay","uzbekistan","vanuatu","vatican city","venezuela",
        "vietnam","yemen","zambia","zimbabwe"
    ]
    
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
            print(f"Fetching RSS feed: {feed_url} (limit={limit})")
            feed = feedparser.parse(feed_url, request_headers={'User-Agent': 'Mozilla/5.0 (compatible; NewsAggregator/1.0)'})
            articles = []
            
            if feed.bozo:
                print(f"Warning: Feed parsing issue in {feed_url}: {feed.bozo_exception}")
            
            if not getattr(feed, 'entries', None):
                print(f"No entries in feed: {feed_url}")

            for entry in feed.entries[:limit]:
                published_parsed = entry.get('published_parsed') or entry.get('updated_parsed')
                articles.append({
                    'title': entry.get('title', 'N/A'),
                    'summary': entry.get('summary', entry.get('description', 'No summary available')),
                    'url': entry.get('link', '#'),
                    'source': feed.feed.get('title', 'Unknown'),
                    'published_at': entry.get('published', 'Unknown'),
                    'published_parsed': published_parsed,
                    'image': ''
                })
            
            print(f"Fetched {len(articles)} entries from {feed_url}")
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
    
    def search_articles(self, query: str = None, keywords: List[str] = None, limit: int = 15) -> List[Dict]:
        """
        Fetch articles and filter by query/keywords
        
        Args:
            query: Search keyword (e.g., 'Lebanon', 'technology')
            keywords: Optional list of keywords to match (case-insensitive OR)
            limit: Maximum articles to return
        
        Returns:
            Filtered list of articles
        """
        all_articles = self.fetch_all_feeds(limit_per_feed=10)

        # Conflict terms and always-include countries
        conflict_terms = ["war", "attack", "crisis", "ceasefire"]
        focus_countries = ["lebanon", "israel", "usa", "united states", "u s"]

        def normalize(text: str) -> str:
            return re.sub(r"[^a-z0-9']+", " ", text.lower()).strip()

        def has_term(norm_text: str, term: str) -> bool:
            if " " in term:
                return term in norm_text
            tokens = set(norm_text.split())
            return term in tokens

        def matches(article):
            text = f"{article.get('title','')} {article.get('summary','')}"
            norm_text = normalize(text)

            has_focus = any(has_term(norm_text, c) for c in focus_countries)
            has_conflict = any(has_term(norm_text, t) for t in conflict_terms)
            has_country = any(has_term(norm_text, c) for c in self.COMMON_COUNTRIES)

            if not (has_focus or (has_conflict and has_country)):
                return False

            # Date filter: only articles in last 24 hours, if parse available
            parsed = article.get('published_parsed')
            if parsed:
                pub_dt = datetime.fromtimestamp(time.mktime(parsed))
                if pub_dt < datetime.now() - timedelta(days=1):
                    return False
            # if no date, we allow it (help avoid totally empty results)

            return True

        filtered = [article for article in all_articles if matches(article)]
        print(f"RSS fetch: {len(all_articles)} total, {len(filtered)} filtered")
        if filtered:
            print("Sample articles:")
            for a in filtered[:3]:
                print(f" - {a.get('title','N/A')} ({a.get('source','Unknown')})")
        else:
            print("No filtered articles matched query/keywords")
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
