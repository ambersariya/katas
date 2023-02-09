from unittest.mock import call

import pytest

from src.core.errors import PilotFlyingHoursExceeded
from src.flight import FlightPairing
from tests.constants import JOHN_SMITH, JANE_DOE, ROUTE_LHR_LAX, PILOT_JANE_DOE, \
    PILOT_JOHN_SMITH


def test_should_generate_a_flight_pairing(pilot_service, mock_pilot_repository):
    mock_pilot_repository.find_by_name.side_effect = [PILOT_JOHN_SMITH, PILOT_JANE_DOE]
    result = pilot_service.generate_pairing(
        pilots=[JOHN_SMITH, JANE_DOE],
        route=ROUTE_LHR_LAX
    )

    assert type(result) == FlightPairing
    mock_pilot_repository.find_by_name.assert_has_calls = [call(JOHN_SMITH), call(JANE_DOE)]


def test_should_generate_a_flight_pairing_when_they_less_than_100_hours_for_the_month(
        pilot_service,
        mock_pilot_repository
):
    mock_pilot_repository.find_by_name.side_effect = [PILOT_JOHN_SMITH, PILOT_JANE_DOE]
    PILOT_JOHN_SMITH.worked_month_hours = 11
    PILOT_JOHN_SMITH.worked_week_hours = 11

    PILOT_JANE_DOE.worked_month_hours = 11
    PILOT_JANE_DOE.worked_week_hours = 11

    result = pilot_service.generate_pairing(
        pilots=[JOHN_SMITH, JANE_DOE],
        route=ROUTE_LHR_LAX
    )

    mock_pilot_repository.save.assert_has_calls([
        call(pilot=PILOT_JOHN_SMITH),
        call(pilot=PILOT_JANE_DOE)
    ])

    assert type(result) == FlightPairing


@pytest.mark.parametrize(
    "captain_month_hours, copilot_month_hours",
    [
        (50, 100),
        (100, 50),
    ]
)
def test_should_raise_exception_when_monthly_hours_exceed_100(captain_month_hours, copilot_month_hours,
                                                              mock_pilot_repository, pilot_service):
    PILOT_JOHN_SMITH.worked_month_hours = captain_month_hours
    PILOT_JOHN_SMITH.worked_week_hours = 11

    PILOT_JANE_DOE.worked_month_hours = copilot_month_hours
    PILOT_JANE_DOE.worked_week_hours = 11

    mock_pilot_repository.find_by_name.side_effect = [PILOT_JOHN_SMITH, PILOT_JANE_DOE]

    with pytest.raises(PilotFlyingHoursExceeded):
        pilot_service.generate_pairing(
            pilots=[JOHN_SMITH, JANE_DOE],
            route=ROUTE_LHR_LAX
        )
