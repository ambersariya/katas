import pytest

from guess_who.guess_who import GuessWho

# def test_should_tell_that_guess_was_done_in_one_turn_when_there_is_only_one_person_to_guess_from():
#     characters = [
#         ["Amelie", ["Female", "Hat", "Brown hair", "Small mouth", "Long hair", "Brown eyes", "Small nose"]],
#     ]
#
#     game = GuessWho(character="Amelie", game_characters=characters)
#     result = game.guess("Female")
#     assert set(result) == {"Correct! in 1 turn"}

test_params_for_correct_guess = [
    ("Amelie", "Female", {'Mirabelle', 'Isabelle', 'Christine', 'Amelie', 'Charline'}),
    ("Amelie", "Hat", {'Henri', 'Amelie', 'Damien', 'Isabelle', 'Bernard'}),
]


@pytest.mark.parametrize(
    "selected_character, guess, expected_outcome", test_params_for_correct_guess
)
def test_should_return_all_the_remaining_character_names_from_a_correct_character_guess(
        selected_character, guess, expected_outcome, game_characters_testdata
):
    game = GuessWho(character=selected_character, game_characters=game_characters_testdata)
    result = game.guess(guess)
    assert set(result) == expected_outcome


test_params_for_incorrect_guess = [
    ("Amelie", "Male", {'Mirabelle', 'Isabelle', 'Christine', 'Amelie', 'Charline'}),
    ("Amelie", "Blue eyes",
     {'Amelie', 'Antonin', 'Benoit', 'Bernard', 'Charline', 'Cecilian', 'Damien', 'Dylan', 'Etienne', 'Henri',
      'Herbert',
      'Isabelle', 'Jean-Claude', 'Lionel', 'Luc', 'Michel', 'Mirabelle', 'Pierre',
      'Renaud'}),

    # Amelie does not have blue eyes
    # return everybody else who doesn't have blue eyes
    # NOTE: we can't return everybody else who has brown eyes because we don't know the type of characteristic
    # ("Amelie", "Mustache", {'Pierre', 'Benoit', 'Lionel', 'Renaud'}),
    # ("Amelie", "Beard", {'Michel', 'Benoit', 'Dylan'}),
    # ("Amelie", "Earrings", {'Mirabelle'})
    # ---------
    # ("Amelie", "Male", {'Mirabelle', 'Isabelle', 'Christine', 'Amelie', 'Charline'}),
    # ("Amelie", "Female", {
    #     'Antonin', 'Benoit', 'Bernard', 'Cecilian', 'Damien', 'Dylan', 'Etienne', 'Henri', 'Herbert', 'Jean',
    #     'Jean-Claude', 'Lionel', 'Luc', 'Michel', 'Owen', 'Pierre', 'Pierre-Louis', 'Renaud', 'Robert'}),
    # ("Amelie", "Male", {'Mirabelle', 'Isabelle', 'Christine', 'Amelie', 'Charline'}),
    # (
    #     "Amelie", "Blue eyes",
    #     {'Amelie', 'Antonin', 'Benoit', 'Bernard', 'Cecilian', 'Damien', 'Dylan', 'Etienne', 'Henri',
    #      'Herbert', 'Isabelle', 'Jean-Claude', 'Lionel', 'Luc', 'Michel', 'Mirabelle', 'Pierre',
    #      'Renaud'}),
    # ("Amelie", "Brown eyes", {'Christine', 'Robert', 'Pierre-Louis', 'Jean', 'Owen'}),
]


@pytest.mark.parametrize(
    "selected_character, incorrect_guess, expected_outcome", test_params_for_incorrect_guess
)
def test_should_return_all_the_remaining_characters_from_an_incorrect_characteristic_guess(
        selected_character, incorrect_guess, expected_outcome, game_characters_testdata
):
    game = GuessWho(character=selected_character, game_characters=game_characters_testdata)
    result = game.guess(incorrect_guess)
    assert set(result) == expected_outcome


def test_should_tell_me_i_have_made_correct_guess_in_turns(game_characters_testdata):
    selected_character = "Amelie"
    guess = "Amelie"
    expected_result = {"Correct! in 1 turns"}
    game = GuessWho(character=selected_character, game_characters=game_characters_testdata)
    result = game.guess(guess)
    assert result == expected_result
