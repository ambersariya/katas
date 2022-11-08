import pytest

from merchants_guide_to_galaxy.answer_queries_use_case import answer_queries_use_case


@pytest.mark.parametrize('input_data, answer, symbol_values', [
    ("how much is pish tegj glob glob ?", "pish tegj glob glob is 42", ["X", "L", "I", "I"])
])
def test_answer_queries_use_case(input_data, answer, symbol_values, mocked_symbol_repo):
    answers = answer_queries_use_case(raw_data=input_data, symbol_repo=mocked_symbol_repo)
    mocked_symbol_repo.symbol_value.side_effect = symbol_values

    assert len(answers) == 1
