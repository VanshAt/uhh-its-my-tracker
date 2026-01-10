# 🎯 Vansh's Valorant Performance Dashboard

A comprehensive Streamlit web application for tracking and analyzing Valorant gameplay performance. This dashboard provides detailed insights into match statistics, agent performance, and climb progress.

## Features

- **Performance Metrics**: Track K/D ratio, ADR, ACS, headshot percentage, and more
- **Agent Analysis**: Analyze performance across different agents
- **Map Statistics**: View performance on different maps
- **Win/Loss Trends**: Visualize match results over time
- **Interactive Charts**: Built with Plotly for dynamic data exploration
- **Data Upload**: Support for custom CSV data uploads

## Technologies Used

- **Streamlit**: For the web interface
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive visualizations
- **NumPy**: Numerical computations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/VanshAt/uhh-its-my-tracker.git
cd uhh-its-my-tracker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Usage

- Upload your own `valorant_matches.csv` file via the sidebar
- Use filters to analyze specific date ranges
- Explore various charts and metrics to gain insights into your gameplay

## Data Format

The CSV should contain columns like:
- Date
- Map
- Mode
- Round_Score
- Agent
- Rank
- Result
- K, D, A (Kills, Deaths, Assists)
- KD, HS%, ADR, ACS
- Performance_Score
- Position
- MVP

## Contributing

Feel free to fork and contribute to this project!

## License

This project is open source and available under the [MIT License](LICENSE).