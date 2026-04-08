# Token Mapper
from typing import Dict, Any, List
import re

class TokenMapper:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
    
    def map_narrative_to_tokens(self, 
                               narrative_analysis: Dict[str, Any],
                               token_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Map narratives to related tokens"""
        narrative_tokens = {}
        
        # For each narrative category, find related tokens
        for category, score in narrative_analysis.get("narrative_distribution", {}).items():
            if score > 0:
                related_tokens = []
                
                # Find tokens related to this narrative
                for token in token_data:
                    token_name = token.get("name", "").lower()
                    token_symbol = token.get("symbol", "").lower()
                    
                    # Check if token name/symbol matches narrative keywords
                    keywords = self.config["narratives"]["keywords"].get(category, [])
                    for keyword in keywords:
                        if keyword.lower() in token_name or keyword.lower() in token_symbol:
                            related_tokens.append(token)
                            break
                
                if related_tokens:
                    narrative_tokens[category] = {
                        "score": score,
                        "tokens": related_tokens
                    }
        
        return narrative_tokens
    
    def calculate_performance_correlation(self, 
                                          narrative_tokens: Dict[str, Any],
                                          price_data: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate performance correlation for narrative-related tokens"""
        performance_data = {}
        
        for category, data in narrative_tokens.items():
            category_perf = []
            
            for token in data["tokens"]:
                token_id = token.get("id")
                if token_id in price_data:
                    # Get performance metrics
                    token_perf = price_data[token_id].get("performance", {})
                    category_perf.append({
                        "token": token,
                        "performance": token_perf
                    })
            
            if category_perf:
                performance_data[category] = {
                    "tokens": category_perf,
                    "avg_performance": self._calculate_average_performance(category_perf)
                }
        
        return performance_data
    
    def _calculate_average_performance(self, token_performances: List[Dict[str, Any]]) -> float:
        """Calculate average performance across tokens"""
        if not token_performances:
            return 0.0
        
        total_perf = 0.0
        count = 0
        
        for token_perf in token_performances:
            perf = token_perf.get("performance", {}).get("7d_change", 0)
            total_perf += perf
            count += 1
        
        return total_perf / count if count > 0 else 0.0