import pytest

from src.core.errors import UnknownPilotException
from src.core.value_objects import PilotName
from src.pilot import Pilot
from tests.constants import JOHN_SMITH, PILOT_JOHN_SMITH


def test_should_find_a_pilot_by_given_name(pilot_repository):
    pilot_repository.add(PILOT_JOHN_SMITH)

    result = pilot_repository.find_by_name(pilot_name=JOHN_SMITH)

    assert isinstance(result, Pilot)


def test_should_not_find_unknown_pilot(pilot_repository):
    with pytest.raises(UnknownPilotException):
        pilot_repository.find_by_name(pilot_name=PilotName('UNKNOWN'))
