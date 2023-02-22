SCORES = ["Love", "Fifteen", "Thirty", "Forty"]

class TennisScoreCalculator:

    def score(self, player_1_points: int, player_2_points: int) -> str:
        if player_1_points == 0 and player_2_points == 0:
            return f"Love All"
        return f"{SCORES[player_1_points]} {SCORES[player_2_points]}"


