# Token Narrative Tracker

Scanner che analizza sentiment e narrative trend su X/Reddit/RSS e li mappa sulle performance di token specifici. Genera una "narrative heat map" e identifica i token più influenzati dalle narrative emergenti.

## 🚀 Features

- **Multi-source scraping**: X (ex Twitter), Reddit, RSS feeds
- **Narrative detection**: Identifica automaticamente le narrative trend (AI, DeFi, Gaming, RWA, etc.)
- **Sentiment analysis**: Valuta il sentiment associato a ogni narrativa
- **Token mapping**: Collega le narrative alle performance dei token
- **Heat map generation**: Visualizza le narrative più calde e i token associati
- **Real-time monitoring**: Traccia l'evoluzione delle narrative nel tempo

## 📁 Architecture

```
narrative-tracker/
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
├── config.json
├── src/
│   ├── __init__.py
│   ├── scraper.py      # Scrape X/Reddit/RSS feeds
│   ├── analyzer.py     # Analyze sentiment and narrative trends
│   ├── mapper.py       # Map narratives to token performance
│   ├── reporter.py     # Generate heat map and reports
│   └── tracker.py      # Main orchestrator
└── output/
    ├── narratives.json  # Narrative analysis results
    └── heatmap.json     # Heat map data
```

## 📊 How It Works

1. **Data Collection**: Scraper raccoglie dati da X, Reddit, RSS feeds
2. **Narrative Detection**: Analyzer identifica le narrative trend usando NLP
3. **Sentiment Analysis**: Valuta il sentiment associato a ogni narrativa
4. **Token Mapping**: Mapper collega le narrative ai token crypto
5. **Heat Map Generation**: Reporter crea la visualizzazione delle narrative
6. **Performance Correlation**: Analizza la correlazione tra narrative e prezzi

## 🛠️ Requirements

```txt
requests>=2.31          # HTTP requests
beautifulsoup4>=4.12    # HTML parsing
lxml>=4.9               # XML parsing
feedparser>=6.0         # RSS feed parsing
regex>=2022.10.31       # Regular expressions
textblob>=0.17.1        # Sentiment analysis
vaderSentiment>=3.3     # Sentiment analysis for social media
scikit-learn>=1.3       # Machine learning for narrative detection
matplotlib>=3.7         # Heat map visualization
seaborn>=0.12           # Heat map styling
```

## 🎮 Usage

```python
from narrative_tracker.tracker import NarrativeTracker

tracker = NarrativeTracker(config_path="config.json")
results = tracker.run()

# Get narrative heat map
heat_map = results.get_heat_map()

# Get top tokens by narrative
top_tokens = results.get_top_tokens_by_narrative("AI")

# Save output
tracker.save_output()
```

## 📋 Output

```json
{
  "timestamp": "2026-04-08T10:00:00Z",
  "narratives": [
    {
      "name": "AI agents",
      "sentiment": 0.75,
      "momentum": 0.82,
      "related_tokens": ["AGIX", "FET", "OCEAN", "NMR"],
      "performance": {"AGIX": 0.15, "FET": 0.12, ...}
    }
  ],
  "heat_map": [
    ["AI", 0.82, ["AGIX", "FET", "OCEAN"]],
    ["DeFi", 0.65, ["UNI", "AAVE", "COMP"]],
    ...
  ]
}
```

## ⚡ Why It's Useful

- **Early Trend Detection**: Identifica le narrative emergenti prima che influenzino i prezzi
- **Token Discovery**: Trova token correlati a narrative calde
- **Market Sentiment**: Capisce il mood del mercato
- **Investment Strategy**: Aiuta a costruire strategie basate su narrative

## 📄 License

MIT - Open source e modificabile.