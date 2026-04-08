#!/usr/bin/env python3

"""
Token Narrative Tracker - Example Usage

This script demonstrates how to use the Token Narrative Tracker system.
"""

from narrative_tracker.tracker import NarrativeTracker

def main():
    # Initialize the tracker
    tracker = NarrativeTracker(config_path="config.json")
    
    # Run the analysis (would need API keys for full functionality)
    # For now, it runs with dummy data
    results = tracker.run()
    
    # Print the heat map
    print("\n=== Narrative Heat Map ===")
    if results and "heat_map" in results:
        for item in results["heat_map"]:
            print(f"{item['narrative']}: Score={item['score']:.3f}, Top Tokens={item['top_tokens']}, Avg Performance={item.get('avg_performance', 0):.2%}")
    else:
        print("No heat map generated")
    
    # Save outputs
    outputs = tracker.save_output()
    print(f"\nOutputs saved to: {outputs}")
    
    return results

if __name__ == "__main__":
    main()