MINIMUM_THRESHOLD_FOR_DEUCE = 4
ADVANTAGE_THRESHOLD = 3
SCORE_DIFF_ADVANTAGE = 1
SCORE_DIFF_WIN = 2
WIN_THRESHOLD = 4


class TennisScoreCalculator:
    SCORES = ["Love", "Fifteen", "Thirty", "Forty"]

    def score(self, player_one_score: int, player_two_score: int) -> str:
        if player_two_score == 0 and player_one_score == 0:
            return "Love All"

        if self.__is_deuce(player_one_score, player_two_score):
            return "Deuce"

        if self.__has_been_won(player_one_score, player_two_score):
            player_with_advantage = self.__player_with_advantage(player_one_score, player_two_score)
            return f"{player_with_advantage} Wins"

        if self.__has_advantage(player_one_score, player_two_score):
            player_with_advantage = self.__player_with_advantage(player_one_score, player_two_score)
            return f"Advantage {player_with_advantage}"

        return f"{self.SCORES[player_one_score]} - {self.SCORES[player_two_score]}"

    @staticmethod
    def __player_with_advantage(player_one_score, player_two_score):
        player_with_advantage = 'Player One' if player_one_score > player_two_score else 'Player Two'
        return player_with_advantage

    def __has_advantage(self, player_one_score: int, player_two_score: int) -> bool:
        score_diff = self.__score_difference(player_one_score, player_two_score)
        return (player_one_score >= ADVANTAGE_THRESHOLD and player_two_score >= ADVANTAGE_THRESHOLD) \
            and score_diff == SCORE_DIFF_ADVANTAGE

    @staticmethod
    def __is_deuce(player_one_score: int, player_two_score: int) -> bool:
        return (
                player_one_score >= MINIMUM_THRESHOLD_FOR_DEUCE and player_two_score >= MINIMUM_THRESHOLD_FOR_DEUCE) \
            and (player_one_score == player_two_score)

    def __has_been_won(self, player_one_score: int, player_two_score: int) -> bool:
        score_diff = self.__score_difference(player_one_score, player_two_score)
        return (player_one_score >= WIN_THRESHOLD and player_two_score >= WIN_THRESHOLD) \
            and (score_diff == SCORE_DIFF_WIN)

    @staticmethod
    def __score_difference(player_one_score, player_two_score):
        return abs(player_one_score - player_two_score)
