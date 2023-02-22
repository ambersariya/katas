import pytest

from tennis_v3.tennis_score_calculator import TennisScoreCalculator

@pytest.mark.parametrize(
    "player_1_points, player_2_points, expected_score", [
        (0,0, "Love All"),
        (1,0, "Fifteen Love"),
        (2,0, "Thirty Love"),
        (3,0, "Forty Love"),
        (0,1, "Love Fifteen"),
        (0,2, "Love Thirty"),
        (0,3, "Love Forty")
    ]
)
def test_calculator_should_return_expected_score_for_player_one_and_player_two(player_1_points, player_2_points, expected_score):
    result = TennisScoreCalculator().score(player_1_points=player_1_points, player_2_points=player_2_points)
    assert result == expected_score
