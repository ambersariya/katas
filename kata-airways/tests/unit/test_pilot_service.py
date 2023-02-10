from unittest.mock import call

import pytest

from src.core.errors import PilotFlyingHoursExceeded, InsufficientPilotsException
from src.core.value_objects import FlyingHours
from src.flight import FlightPairing
from tests.constants import JOHN_SMITH, JANE_DOE, ROUTE_LHR_LAX, PILOT_JANE_DOE, \
    PILOT_JOHN_SMITH


def test_should_generate_a_flight_pairing(pilot_service, mock_pilot_repository):
    mock_pilot_repository.find_by_availability.return_value = [PILOT_JOHN_SMITH, PILOT_JANE_DOE]
    result = pilot_service.generate_pairing(route=ROUTE_LHR_LAX)
    assert type(result) == FlightPairing
    mock_pilot_repository.find_by_availability.assert_has_calls = [call(JOHN_SMITH), call(JANE_DOE)]


def test_should_generate_a_flight_pairing_when_they_less_than_100_hours_for_the_month(
        pilot_service,
        mock_pilot_repository
):
    mock_pilot_repository.find_by_availability.return_value = [PILOT_JOHN_SMITH, PILOT_JANE_DOE]
    PILOT_JOHN_SMITH.worked_month_hours = 11
    PILOT_JOHN_SMITH.worked_week_hours = 11

    PILOT_JANE_DOE.worked_month_hours = 11
    PILOT_JANE_DOE.worked_week_hours = 11

    result = pilot_service.generate_pairing(route=ROUTE_LHR_LAX)
    mock_pilot_repository.add.assert_has_calls([
        call(pilot=PILOT_JOHN_SMITH),
        call(pilot=PILOT_JANE_DOE)
    ])

    assert type(result) == FlightPairing


def test_should_raise_exception_when_we_find_no_one_to_create_flight_pairing(pilot_service, mock_pilot_repository):
    mock_pilot_repository.find_by_availability.return_value = []
    with pytest.raises(InsufficientPilotsException):
        pilot_service.generate_pairing(route=ROUTE_LHR_LAX)


@pytest.mark.skip('Come back to this when we\'ve worked out rule')
@pytest.mark.parametrize(
    "captain_hours, copilot_hours",
    [
        # Monthly hours
        pytest.param(FlyingHours(month=100, week=11), FlyingHours(month=50, week=11)),
        pytest.param(FlyingHours(month=89, week=11), FlyingHours(month=50, week=11)),
        pytest.param(FlyingHours(month=50, week=11), FlyingHours(month=100, week=11)),
        pytest.param(FlyingHours(month=100, week=11), FlyingHours(month=100, week=11)),
        pytest.param(FlyingHours(month=100, week=11), FlyingHours(month=89, week=11)),
        # Week hours
        pytest.param(FlyingHours(month=50, week=19), FlyingHours(month=50, week=11)),
        pytest.param(FlyingHours(month=50, week=11), FlyingHours(month=50, week=20)),
        pytest.param(FlyingHours(month=50, week=11), FlyingHours(month=50, week=30)),
        pytest.param(FlyingHours(month=50, week=25), FlyingHours(month=50, week=25)),
    ]
)
def test_should_raise_exception_when_flying_hours_exceed_threshold(
        captain_hours, copilot_hours, mock_pilot_repository, pilot_service
):
    PILOT_JOHN_SMITH.worked_month_hours = captain_hours.month
    PILOT_JOHN_SMITH.worked_week_hours = captain_hours.week

    PILOT_JANE_DOE.worked_month_hours = copilot_hours.month
    PILOT_JANE_DOE.worked_week_hours = copilot_hours.week

    mock_pilot_repository.find_by_availability.return_value = [PILOT_JOHN_SMITH, PILOT_JANE_DOE]

    with pytest.raises(PilotFlyingHoursExceeded):
        pilot_service.generate_pairing(route=ROUTE_LHR_LAX)
