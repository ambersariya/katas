from unittest.mock import patch

from merchants_guide_to_galaxy.usecase.answer_queries_use_case import Answer


@patch('builtins.print')
def test_should_print_answer_from_a_list_of_answers(mocked_print, answer_printer):
    expected_answers = "some outcome\n" \
                       "meaning of life is 42"

    answers = [
        Answer(query="blah blah blah is?", outcome="some outcome"),
        Answer(query="what is the meaning of life?", outcome="meaning of life is 42"),
    ]

    answer_printer.print(answers=answers)
    mocked_print.assert_called_with(expected_answers)
