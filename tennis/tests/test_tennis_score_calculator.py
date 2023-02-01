import pytest

from tennis.tennis_score_calculator import TennisScoreCalculator


@pytest.fixture
def tennis_score_calculator():
    return TennisScoreCalculator()


@pytest.mark.parametrize(
    'player_one_score, player_two_score, expected_result',
    [
        (0, 0, "Love All"),
        (1, 0, "Fifteen Love"),
        (2, 0, "Thirty Love"),
        (3, 0, "Forty Love"),
        (0, 1, "Love Fifteen"),
        (0, 2, "Love Thirty"),
        (0, 3, "Love Forty"),
        (3, 3, "Deuce"),
        (4, 4, "Deuce"),
        (5, 5, "Deuce"),
        (3, 4, "Advantage Player Two"),
        (5, 4, "Advantage Player One"),
        (5, 3, "Player One Wins"),
        (3, 5, "Player Two Wins"),
    ]
)
def test_should_return_calculated_score_for_players(
        tennis_score_calculator, player_one_score, player_two_score, expected_result
):
    result = tennis_score_calculator.score(player_one_score, player_two_score)
    assert result == expected_result
