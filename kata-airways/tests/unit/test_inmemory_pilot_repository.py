import pytest

from src.core.errors import UnknownPilotException
from src.core.value_objects import PilotName
from src.pilot import Pilot
from tests.constants import JOHN_SMITH, PILOT_JOHN_SMITH, PILOT_JANE_DOE


def test_should_find_a_pilot_by_given_name(pilot_repository):
    pilot_repository.add(PILOT_JOHN_SMITH)

    result = pilot_repository.find_by_name(pilot_name=JOHN_SMITH)

    assert isinstance(result, Pilot)


def test_should_not_find_unknown_pilot(pilot_repository):
    with pytest.raises(UnknownPilotException):
        pilot_repository.find_by_name(pilot_name=PilotName('UNKNOWN'))


def test_should_find_pilot_who_has_worked_less_than_30_hours_for_the_week(pilot_repository):
    PILOT_JOHN_SMITH.worked_month_hours = 25
    PILOT_JOHN_SMITH.worked_week_hours = 20

    PILOT_JANE_DOE.worked_week_hours = 30
    PILOT_JANE_DOE.worked_month_hours = 99

    pilot_repository.add(PILOT_JOHN_SMITH)
    pilot_repository.add(PILOT_JANE_DOE)

    result = pilot_repository.find_by_availability()

    assert len(result) == 1
    assert result[0].name == JOHN_SMITH
    assert result[0].worked_week_hours <= 30
    assert result[0].worked_month_hours <= 100
