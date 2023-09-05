import pytest

from py_poker_hands.poker import Poker


@pytest.fixture
def poker():
    return Poker()


def test_be_able_to_declare_player_2_as_the_winner(poker):
    cards = "2H 3D 5S 9C KD 2C 3H 4S 8C AH"
    poker.parse(cards=cards)
    output = poker.check_winner()
    assert "Player 2 wins." == output


def test_be_able_to_declare_player_2_as_the_winner(poker):
    cards = "2H 3D 5S 9C KD 2C 3H 4S 8C AH"
    poker.parse(cards=cards)
    output = poker.check_winner()

    assert "Player 2 wins." == output
