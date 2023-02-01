from enum import Enum


class TennisScores(Enum):
    Love = 0
    Fifteen = 1
    Thirty = 2
    Forty = 3

    def __str__(self) -> str:
        return self.name


class GameState(Enum):
    Advantage = 'Advantage'
    Wins = 'Wins'
    Deuce = "Deuce"
    Love_All = "Love All"

    def __str__(self) -> str:
        return self.name


class TennisScoreCalculator:
    ID_PLAYER_TWO = "Player Two"
    ID_PLAYER_ONE = "Player One"
    MIN_SCORE_FOR_ADVANTAGE = 3
    SCORE_DIFF_FOR_DEUCE = 0
    SCORE_DIFF_FOR_ADVANTAGE = 1
    SCORE_DIFF_FOR_WIN = 2

    def score(self, player_one_score: int, player_two_score: int) -> str:
        if self.__is_deuce(player_one_score, player_two_score):
            return str(GameState.Deuce)

        if self.__has_advantage(player_one_score, player_two_score):
            player = self.__player_with_advantage(player_one_score, player_two_score)
            return f"{GameState.Advantage} {player}"

        if self.__winner(player_one_score, player_two_score):
            player = self.__player_with_advantage(player_one_score, player_two_score)
            return f"{player} {GameState.Wins}"

        return self.__generate_score(player_one_score, player_two_score)

    def __winner(self, player_one_score: int, player_two_score: int) -> bool:
        return self.__min_three_points_each(player_one_score, player_two_score) \
            and self.__score_difference(player_one_score, player_two_score) == self.SCORE_DIFF_FOR_WIN

    def __is_deuce(self, player_one_score, player_two_score) -> bool:
        return self.__min_three_points_each(player_one_score, player_two_score) \
            and self.__score_difference(player_one_score, player_two_score) == self.SCORE_DIFF_FOR_DEUCE

    def __has_advantage(self, player_one_score: int, player_two_score: int) -> bool:
        return self.__min_three_points_each(player_one_score, player_two_score) \
            and self.__score_difference(player_one_score, player_two_score) == self.SCORE_DIFF_FOR_ADVANTAGE

    def __generate_score(self, player_one_score: int, player_two_score: int) -> str:

        calculated_player_one_score = self.__calculate_player_score(player_one_score)
        calculated_player_two_score = self.__calculate_player_score(player_two_score)

        if calculated_player_one_score == TennisScores.Love.name \
                and calculated_player_two_score == TennisScores.Love.name:
            return GameState.Love_All.value

        return f"{calculated_player_one_score} {calculated_player_two_score}"

    @staticmethod
    def __min_three_points_each(player_one_score: int, player_two_score: int) -> bool:
        return player_one_score >= TennisScoreCalculator.MIN_SCORE_FOR_ADVANTAGE \
            and player_two_score >= TennisScoreCalculator.MIN_SCORE_FOR_ADVANTAGE

    @staticmethod
    def __calculate_player_score(player_score: int) -> str:
        return TennisScores(player_score).name

    @staticmethod
    def __score_difference(player_one_score: int, player_two_score: int) -> int:
        return abs(player_one_score - player_two_score)

    @staticmethod
    def __player_with_advantage(player_one_score: int, player_two_score: int) -> str:
        return TennisScoreCalculator.ID_PLAYER_ONE if player_one_score > player_two_score \
            else TennisScoreCalculator.ID_PLAYER_TWO
