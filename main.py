from src.bundesliga_analysis import BundesligaAnalysis


def main() -> None:
    """
    Run Bundesliga analysis pipeline.
    """

    analyzer = BundesligaAnalysis(
        "data/1_bundesliga_overall.csv"
    )

    analyzer.load_data()
    analyzer.clean_data()

    top_teams = analyzer.calculate_top_teams()

    print(top_teams)

    analyzer.save_results(
        top_teams,
        "output/top_5_teams_avg_goals.csv"
    )


if __name__ == "__main__":
    main()