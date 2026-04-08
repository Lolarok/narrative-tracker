# Narrative Analyzer
from typing import Dict, Any, List
from datetime import datetime, timedelta
import re
from collections import Counter

class NarrativeAnalyzer:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.narrative_keywords = config["narratives"]["keywords"]
    
    def analyze_post(self, post: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Analyze a single post for narrative mentions"""
        narratives = []
        
        title = post.get("title", "").lower()
        summary = post.get("summary", "").lower()
        content = post.get("content", "").lower()
        
        # Combine all text
        full_text = f"{title} {summary} {content}"
        
        # Check each narrative category
        for category, keywords in self.narrative_keywords.items():
            count = 0
            for keyword in keywords:
                if keyword.lower() in full_text:
                    count += 1
            
            if count > 0:
                narratives.append({
                    "category": category,
                    "mentions": count,
                    "confidence": min(1.0, count / len(keywords) + 0.2)
                })
        
        return narratives
    
    def analyze_all(self, posts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze all posts and aggregate results"""
        narrative_counts = {cat: 0 for cat in self.narrative_keywords.keys()}
        sentiment_scores = {}
        momentum_scores = {}
        
        for post in posts:
            post_narratives = self.analyze_post(post)
            
            for narrative in post_narratives:
                category = narrative["category"]
                narrative_counts[category] = narrative_counts.get(category, 0) + narrative["mentions"]
                
                # Track sentiment if available
                if "sentiment" in post:
                    sentiment_scores[category] = sentiment_scores.get(category, []) + [post["sentiment"]]
                
                # Track momentum (based on time decay)
                published = post.get("published", "")
                # Would calculate momentum based on recency
        
        # Calculate percentages
        total_mentions = sum(narrative_counts.values())
        if total_mentions > 0:
            for category in narrative_counts:
                narrative_counts[category] = narrative_counts[category] / total_mentions
        
        return {
            "narrative_distribution": narrative_counts,
            "sentiment_scores": sentiment_scores,
            "momentum_scores": momentum_scores
        }