import pytest

from tennis_v2.tennis_score_calculator import TennisScoreCalculator


@pytest.mark.parametrize('player_one_score, player_two_score, expected_result',
                         [(0, 0, "Love All"),
                          (0, 1, "Love - Fifteen"),
                          (0, 2, "Love - Thirty"),
                          (0, 3, "Love - Forty"),
                          (1, 0, "Fifteen - Love"),
                          (2, 0, "Thirty - Love"),
                          (3, 0, "Forty - Love"),
                          (4, 4, "Deuce"),
                          (5, 5, "Deuce"),
                          (3, 3, "Forty - Forty"),
                          (4, 3, "Advantage Player One"),
                          (3, 4, "Advantage Player Two"),
                          (6, 4, "Player One Wins"),
                          (4, 6, "Player Two Wins")
                          ]
                         )
def test_should_return_a_scoreboard_the_expected_result_when_the_players_scores_are_given(player_one_score,
                                                                                          player_two_score,
                                                                                          expected_result):
    result = TennisScoreCalculator().score(player_one_score=player_one_score,
                                           player_two_score=player_two_score)
    assert result == expected_result
