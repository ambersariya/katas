class Poker:
    def parse(self, cards: str) -> str:
        pass

    def check_winner(self) -> str:
        raise NotImplementedError()


def test_should_calculate_winner_when_two_players_are_playing():
    cards = "2H 3D 5S 9C KD 2C 3H 4S 8C AH"
    poker = Poker()
    poker.parse(cards=cards)
    output = poker.check_winner()

    assert output == "Player 2 wins."
