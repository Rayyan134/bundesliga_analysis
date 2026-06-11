"""
Bundesliga Data Analysis

Loads Bundesliga match data, cleans missing values,
calculates average goals scored by each team,
and exports the top 5 teams to a CSV file.
"""

from pathlib import Path # Used to safely handle file/directory paths across OS platforms

import pandas as pd


class BundesligaAnalysis:
    """
    Bundesliga analysis utility class.
    """

    def __init__(self, file_path: str) -> None:
        """
        Initialise the analysis class.

        Args:
            file_path: Path to Bundesliga CSV file.
        """

        # Store the dataset path for later use.
        self.file_path = file_path

        # DataFrame is initially empty until data is loaded.
        self.df: pd.DataFrame | None = None

    def load_data(self) -> pd.DataFrame:
        """
        Load Bundesliga dataset.

        Returns:
            pd.DataFrame: Loaded dataframe.
        """

        # Read the CSV file into a pandas DataFrame.
        self.df = pd.read_csv(self.file_path)

        return self.df

    def clean_data(self) -> pd.DataFrame:
        """
        Fill missing values in categorical columns.

        Returns:
            pd.DataFrame: Cleaned dataframe.
        """

        if self.df is None:
            raise ValueError("Dataset not loaded")

        # Replace missing stadium and location values
        # with a placeholder to keep the dataset consistent.
        self.df["Location"] = self.df["Location"].fillna("Unknown")
        self.df["Stadium"] = self.df["Stadium"].fillna("Unknown")

        return self.df

    def calculate_top_teams(self) -> pd.DataFrame:
        """
        Calculate top 5 teams by average goals scored.

        Returns:
            pd.DataFrame: Top 5 teams.
        """

        if self.df is None:
            raise ValueError("Dataset not loaded")

        # Total goals scored when playing at home.
        home_goals = (
            self.df.groupby("Home_Team")["Home_Goals"]
            .sum()
        )

        # Total goals scored when playing away.
        away_goals = (
            self.df.groupby("Guest_Team")["Guest_Goals"]
            .sum()
        )

        # Combine home and away goals to get each team's
        # overall goal tally for the season.
        total_goals = home_goals.add(
            away_goals,
            fill_value=0
        )

        # Count matches played at home.
        home_matches = (
            self.df.groupby("Home_Team")
            .size()
        )

        # Count matches played away.
        away_matches = (
            self.df.groupby("Guest_Team")
            .size()
        )

        # Total matches played by each team.
        total_matches = home_matches.add(
            away_matches,
            fill_value=0
        )

        # Calculate average goals scored per match
        # and sort teams from highest to lowest.
        average_goals = (
            total_goals / total_matches
        ).sort_values(
            ascending=False
        )

        # Extract the top five teams and convert
        # the result into a clean tabular format.
        top_5 = (
            average_goals
            .head(5)
            .reset_index()
        )

        # Rename columns for readability.
        top_5.columns = [
            "Team",
            "Average_Goals"
        ]

        return top_5

    def save_results(
        self,
        results: pd.DataFrame,
        output_path: str
    ) -> None:
        """
        Save analysis results to CSV.

        Args:
            results: DataFrame to save.
            output_path: Output CSV path.
        """

        # Create the output directory if it does not exist.
        Path(output_path).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        # Export results without the DataFrame index.
        results.to_csv(
            output_path,
            index=False
        )