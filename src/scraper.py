# Narrative Scraper
import requests
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
import feedparser
import json

class NarrativeScraper:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
    
    def scrape_twitter(self, bearer_token: str) -> List[Dict[str, Any]]:
        """Scrape Twitter/X for recent posts"""
        posts = []
        # Would implement with Twitter API v2
        return posts
    
    def scrape_reddit(self, client_id: str, client_secret: str) -> List[Dict[str, Any]]:
        """Scrape Reddit for posts"""
        posts = []
        # Would implement with PRAW or Pushshift
        return posts
    
    def scrape_rss(self) -> List[Dict[str, Any]]:
        """Scrape RSS feeds"""
        posts = []
        
        for feed_url in self.config["scraping"]["sources"]["rss"]["feeds"]:
            try:
                feed = feedparser.parse(feed_url)
                for entry in feed.entries[:self.config["scraping"]["sources"]["rss"]["max_items"]]:
                    post = {
                        "source": "RSS",
                        "title": entry.get("title", ""),
                        "summary": entry.get("summary", ""),
                        "published": entry.get("published", ""),
                        "link": entry.get("link", ""),
                        "content": self._extract_rss_content(entry)
                    }
                    posts.append(post)
            except Exception as e:
                print(f"Error scraping RSS feed {feed_url}: {e}")
        
        return posts
    
    def _extract_rss_content(self, entry: Dict[str, Any]) -> str:
        """Extract content from RSS entry"""
        # Try different fields to get the full content
        content_fields = ["content", "summary", "description", "content_summary"]
        for field in content_fields:
            if field in entry:
                if isinstance(entry[field], list) and len(entry[field]) > 0:
                    return entry[field][0].get("value", str(entry[field]))
                elif isinstance(entry[field], str):
                    return entry[field]
        return str(entry)
    
    def scrape_all(self, env: Optional[Dict] = None) -> List[Dict[str, Any]]:
        """Scrape all configured sources"""
        all_posts = []
        
        # RSS scraping (doesn't require API keys)
        all_posts.extend(self.scrape_rss())
        
        # Twitter scraping (requires bearer token)
        twitter_token = env.get("TWITTER_BEARER_TOKEN") if env else None
        if twitter_token:
            try:
                all_posts.extend(self.scrape_twitter(twitter_token))
            except Exception as e:
                print(f"Twitter scraping failed: {e}")
        
        # Reddit scraping (requires client ID/secret)
        reddit_client_id = env.get("REDDIT_CLIENT_ID") if env else None
        reddit_client_secret = env.get("REDDIT_CLIENT_SECRET") if env else None
        if reddit_client_id and reddit_client_secret:
            try:
                all_posts.extend(self.scrape_reddit(reddit_client_id, reddit_client_secret))
            except Exception as e:
                print(f"Reddit scraping failed: {e}")
        
        return all_posts