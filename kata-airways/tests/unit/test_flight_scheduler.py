import pytest

from src.core.errors import UnknownDestination
from src.flight_scheduler import InsufficientPilotsForPairing
from src.schedule import Schedule
from tests.constants import JOHN_SMITH, FLIGHT_LHR_LAX_UNPAIRED, ROUTE_LHR_LAX, FLIGHT_LHR_LAX_PAIRED, \
    FLIGHT_PAIR_JOHN_JANE


def test_generate_schedule_should_return_a_schedule(
        flight_scheduler,
        mock_route_map,
        mock_pilot_service
):
    flights = []
    flight_schedule = flight_scheduler.generate_schedule(flights)
    assert type(flight_schedule) == Schedule


def test_generate_schedule_should_create_flight_schedule_for_lax(
        flight_scheduler, mock_route_map, mock_pilot_service
):
    flights = [FLIGHT_LHR_LAX_UNPAIRED]
    mock_route_map.get_route.return_value = ROUTE_LHR_LAX
    mock_pilot_service.generate_pairing.return_value = FLIGHT_PAIR_JOHN_JANE
    expected_schedule = Schedule([FLIGHT_LHR_LAX_PAIRED])

    result = flight_scheduler.generate_schedule(flights)

    assert result == expected_schedule
    mock_route_map.get_route.assert_called_once()
    mock_pilot_service.generate_pairing.assert_called_once()


def test_raise_exception_for_unknown_destination(flight_scheduler, mock_route_map):
    flights = [FLIGHT_LHR_LAX_UNPAIRED]
    mock_route_map.get_route.side_effect = UnknownDestination()
    with pytest.raises(UnknownDestination):
        flight_scheduler.generate_schedule(flights)
        mock_route_map.get_route.assert_called_once_with(origin="LHR", destination="LAX")


def test_should_raise_insufficient_pilots_exception_when_num_of_pilots_is_not_an_even_number(
        flight_scheduler,
        mock_route_map,
        mock_pilot_service
):
    flights = [FLIGHT_LHR_LAX_UNPAIRED]
    mock_route_map.get_route.return_value = ROUTE_LHR_LAX
    mock_pilot_service.generate_pairing.side_effect = InsufficientPilotsForPairing()
    with pytest.raises(InsufficientPilotsForPairing):
        flight_scheduler.generate_schedule(flights)
        mock_route_map.get_route.assert_called_once_with(origin="LAX", destination="LHR")
