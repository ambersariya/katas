from unittest.mock import call

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
