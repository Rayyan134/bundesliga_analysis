# Bundesliga Analysis

A Pandas-based data analysis project using historical German Bundesliga match data.

## Features

- Load Bundesliga match data
- Handle missing values
- Calculate average goals scored per team
- Identify top 5 highest-scoring teams
- Export results to CSV

## Technologies

- Python
- Pandas

## Project Structure

```text
bundesliga-analysis/
│
├── data/
├── output/
├── src/
├── main.py
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Output

```text
output/top_5_teams_avg_goals.csv
```

Contains the top 5 Bundesliga teams ranked by average goals scored.

```csv
Team,Average_Goals
FC Bayern München,2.472340425531915
Borussia Dortmund,1.973049645390071
RB Leipzig,1.9494949494949494
Bayer Leverkusen,1.8411347517730496
Werder Bremen,1.6274217585692996
```
