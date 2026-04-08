# Report Generator
import json
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, Any, List

class ReportGenerator:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
    
    def generate_heat_map(self, 
                          narrative_analysis: Dict[str, Any],
                          performance_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate narrative heat map"""
        heat_map = []
        
        # Get narrative distribution
        narrative_dist = narrative_analysis.get("narrative_distribution", {})
        
        for category, score in narrative_dist.items():
            if score >= self.config["output"]["min_momentum"]:
                # Get top performing tokens for this narrative
                perf_data = performance_data.get(category, {})
                tokens = perf_data.get("tokens", [])[:3]  # Top 3 tokens
                
                heat_map.append({
                    "narrative": category,
                    "score": score,
                    "top_tokens": [token["token"]["symbol"] for token in tokens],
                    "avg_performance": perf_data.get("avg_performance", 0)
                })
        
        # Sort by score
        heat_map.sort(key=lambda x: x["score"], reverse=True)
        
        return heat_map
    
    def generate_full_report(self, 
                           narrative_analysis: Dict[str, Any],
                           performance_data: Dict[str, Any],
                           timestamp: str) -> Dict[str, Any]:
        """Generate complete report"""
        report = {
            "timestamp": timestamp,
            "heat_map": self.generate_heat_map(narrative_analysis, performance_data),
            "narrative_distribution": narrative_analysis.get("narrative_distribution", {}),
            "sentiment_analysis": narrative_analysis.get("sentiment_scores", {}),
            "performance_data": performance_data
        }
        
        return report
    
    def save_heat_map_image(self, 
                           heat_map: Dict[str, Any], 
                           output_path: str = "output/heatmap.png"):
        """Save heat map as image"""
        # Prepare data for plotting
        narratives = [item["narrative"] for item in heat_map]
        scores = [item["score"] for item in heat_map]
        performances = [item["avg_performance"] for item in heat_map]
        
        # Create figure
        fig, ax1 = plt.subplots(figsize=(10, 6))
        
        # Plot narrative scores
        ax1.barh(narratives, scores, color='skyblue', label='Narrative Score')
        ax1.set_xlabel('Narrative Score')
        ax1.set_title('Token Narrative Heat Map')
        ax1.invert_yaxis()
        
        # Create twin axis for performance
        ax2 = ax1.twinx()
        ax2.plot(performances, range(len(performances)), 'ro-', linewidth=2, markersize=8, label='Avg Performance')
        ax2.set_ylabel('Performance (%)')
        
        plt.legend(loc='upper right')
        plt.tight_layout()
        
        # Save figure
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        plt.close()
        
        return output_path