import pytest as pytest

from unittest.mock import patch

@pytest.fixture()
def test_input():
    return """
glob is I
prok is V
pish is X
tegj is L
glob glob Silver is 34 Credits
glob prok Gold is 57800 Credits
pish pish Iron is 3910 Credits
how much is pish tegj glob glob ?
how many Credits is glob prok Silver ?
how many Credits is glob prok Gold ?
how many Credits is glob prok Iron ?
how much wood could a woodchuck chuck if a woodchuck could chuck wood ?
"""


OUTPUT = """
pish tegj glob glob is 42
glob prok Silver is 68 Credits
glob prok Gold is 57800 Credits
glob prok Iron is 782 Credits
I have no idea what you are talking about
"""


@patch('builtins.print')
def test_should_convert_intergalactic_currency_to_credits(mock_print, test_input, intergalactic_currency_converter):
    intergalactic_currency_converter.execute_conversion(test_input)
    mock_print.assert_called_with(OUTPUT)
