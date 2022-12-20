import pytest

from merchants_guide_to_galaxy.domain.currency import Currency, CurrencyValue
from merchants_guide_to_galaxy.domain.error import NonExistingCurrency
from merchants_guide_to_galaxy.domain.metal import Metal
from merchants_guide_to_galaxy.usecase.answer_queries_use_case import answer_queries_use_case, Answer

pish_tegj_glob_glob = [
    Currency(name="pish", value=CurrencyValue.X),
    Currency(name="tegj", value=CurrencyValue.L),
    Currency(name="glob", value=CurrencyValue.I),
    Currency(name="glob", value=CurrencyValue.I)

]

glob_prok_silver = [
    Currency(name="glob", value=CurrencyValue.I),
    Currency(name="prok", value=CurrencyValue.V),
    Metal(name='Silver', value=17)
]

mama_cita_spaceJunk = [
    Currency(name="mama", value=CurrencyValue.I),
    Currency(name="cita", value=CurrencyValue.V),
    Metal(name='spaceJunk', value=17)
]


@pytest.mark.parametrize('input_data, answer, symbol_values, expected_answer', [
    ("how much is pish tegj glob glob ?", "pish tegj glob glob is 42.0", pish_tegj_glob_glob,
     Answer(query='how much is pish tegj glob glob ?', outcome='pish tegj glob glob is 42.0')),
    ("how many Credits is glob prok Silver ?", "glob prok Silver is 68.0 Credits", glob_prok_silver,
     Answer(query='how many Credits is glob prok Silver ?', outcome='glob prok Silver is 68.0 Credits')),
    ("how many Credits is mama cita spaceJunk ?", "mama cita spaceJunk is 68.0 Credits", mama_cita_spaceJunk,
     Answer(query='how many Credits is mama cita spaceJunk ?', outcome='mama cita spaceJunk is 68.0 Credits'))
])
def test_answer_queries_use_case(input_data, answer, symbol_values, expected_answer, mocked_symbol_repo):
    mocked_symbol_repo.find_symbol_value.side_effect = symbol_values
    answers = answer_queries_use_case(raw_data=input_data, symbol_repo=mocked_symbol_repo)

    assert len(answers) == 1
    assert answers[0] == expected_answer


def test_should_give_erroneous_answer_for_invalid_query(mocked_symbol_repo):
    query = "how much is blag blah blog ?"
    expected_answer = Answer(query, "I have no idea what you are talking about")
    mocked_symbol_repo.find_symbol_value.side_effect = NonExistingCurrency()

    answers = answer_queries_use_case(raw_data=query, symbol_repo=mocked_symbol_repo)
    assert len(answers) == 1
    assert answers[0] == expected_answer
