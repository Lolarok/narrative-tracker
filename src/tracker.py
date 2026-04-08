# Narrative Tracker Orchestrator
import json
from datetime import datetime
from typing import Dict, Any, Optional

from .scraper import NarrativeScraper
from .analyzer import NarrativeAnalyzer
from .mapper import TokenMapper
from .reporter import ReportGenerator

class NarrativeTracker:
    def __init__(self, config_path: str = "config.json"):
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        
        # Initialize components
        self.scraper = NarrativeScraper(self.config)
        self.analyzer = NarrativeAnalyzer(self.config)
        self.mapper = TokenMapper(self.config)
        self.reporter = ReportGenerator(self.config)
        
        # Store results
        self.narrative_analysis: Optional[Dict[str, Any]] = None
        self.performance_data: Optional[Dict[str, Any]] = None
        self.heat_map: Optional[Dict[str, Any]] = None
        self.full_report: Optional[Dict[str, Any]] = None
    
    def load_token_data(self) -> List[Dict[str, Any]]:
        """Load token data (would fetch from CoinGecko or local database)"""
        # For now, return dummy data
        return [
            {"id": "bitcoin", "name": "Bitcoin", "symbol": "BTC"},
            {"id": "ethereum", "name": "Ethereum", "symbol": "ETH"},
            {"id": "cardano", "name": "Cardano", "symbol": "ADA"},
            {"id": "solana", "name": "Solana", "symbol": "SOL"},
            {"id": "polkadot", "name": "Polkadot", "symbol": "DOT"},
            {"id": "chainlink", "name": "Chainlink", "symbol": "LINK"},
            {"id": "uniswap", "name": "Uniswap", "symbol": "UNI"},
            {"id": "aave", "name": "Aave", "symbol": "AAVE"},
            {"id": "compound", "name": "Compound", "symbol": "COMP"},
            {"id": "maker", "name": "Maker", "symbol": "MKR"}
        ]
    
    def load_price_data(self) -> Dict[str, Any]:
        """Load price data (would fetch from CoinGecko API)"""
        # Dummy data for now
        return {
            "bitcoin": {"performance": {"7d_change": 0.12}},
            "ethereum": {"performance": {"7d_change": 0.15}},
            "cardano": {"performance": {"7d_change": -0.02}},
            "solana": {"performance": {"7d_change": 0.25}},
            "polkadot": {"performance": {"7d_change": 0.05}}
        }
    
    def run(self, env: Optional[Dict] = None) -> Dict[str, Any]:
        """Main execution pipeline"""
        print("Starting Token Narrative Tracker...")
        
        # Step 1: Scrape content
        print("1. Scraping social media and RSS...")
        posts = self.scraper.scrape_all(env)
        
        if not posts:
            print("No posts found!")
            return {}
        
        # Step 2: Analyze narratives
        print("2. Analyzing narratives...")
        self.narrative_analysis = self.analyzer.analyze_all(posts)
        
        # Step 3: Load token data
        print("3. Loading token data...")
        token_data = self.load_token_data()
        
        # Step 4: Map narratives to tokens
        print("4. Mapping narratives to tokens...")
        self.performance_data = self.mapper.calculate_performance_correlation(
            self.mapper.map_narrative_to_tokens(self.narrative_analysis, token_data),
            self.load_price_data()
        )
        
        # Step 5: Generate heat map
        print("5. Generating narrative heat map...")
        self.heat_map = self.reporter.generate_heat_map(self.narrative_analysis, self.performance_data)
        
        # Step 6: Generate full report
        print("6. Generating full report...")
        self.full_report = self.reporter.generate_full_report(
            self.narrative_analysis,
            self.performance_data,
            datetime.now().isoformat()
        )
        
        print("Done!")
        return self.full_report
    
    def save_output(self, output_dir: str = "output"):
        """Save all output files"""
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        # Save narratives JSON
        narratives_path = f"{output_dir}/narratives.json"
        with open(narratives_path, 'w') as f:
            json.dump(self.narrative_analysis, f, indent=2)
        
        # Save heat map JSON
        heatmap_path = f"{output_dir}/heatmap.json"
        with open(heatmap_path, 'w') as f:
            json.dump(self.heat_map, f, indent=2)
        
        # Save full report
        report_path = f"{output_dir}/report.json"
        with open(report_path, 'w') as f:
            json.dump(self.full_report, f, indent=2)
        
        # Save heat map image
        self.reporter.save_heat_map_image(self.heat_map, f"{output_dir}/heatmap.png")
        
        print(f"Outputs saved to {output_dir}/")
        return {
            "narratives": narratives_path,
            "heatmap": heatmap_path,
            "report": report_path,
            "image": f"{output_dir}/heatmap.png"
        }