import pytest

from src.core.errors import UnknownDestination
from src.core.route_map import RouteMap
from src.core.value_objects import Route, Airport

AIRPORT_LAX = Airport('LAX')
AIRPORT_LHR = Airport('LHR')
AIRPORT_UNKNOWN = Airport('UKN')

ALLOWED_ROUTES = [
    Route(AIRPORT_LHR, AIRPORT_LAX, 11),
    Route(AIRPORT_LAX, AIRPORT_LHR, 11)
]


def test_should_return_true_for_valid_origin_and_destination():
    route_map = RouteMap(allowed_routes=ALLOWED_ROUTES)
    assert route_map.is_valid_route(AIRPORT_LAX, AIRPORT_LHR)


def test_should_return_false_for_invalid_origin_and_destination():
    route_map = RouteMap(allowed_routes=ALLOWED_ROUTES)
    assert route_map.is_valid_route(AIRPORT_UNKNOWN, AIRPORT_LHR) is False


def test_raise_exception_when_origin_and_destination_are_invalid():
    route_map = RouteMap(allowed_routes=ALLOWED_ROUTES)
    with pytest.raises(UnknownDestination):
        route_map.get_route(origin=AIRPORT_LHR, destination=AIRPORT_UNKNOWN)


def test_should_return_the_route_for_given_origin_and_destination():
    route_map = RouteMap(allowed_routes=ALLOWED_ROUTES)
    result = route_map.get_route(origin=AIRPORT_LHR, destination=AIRPORT_LAX)

    assert type(result) == Route
    assert result.origin == AIRPORT_LHR
    assert result.destination == AIRPORT_LAX
    assert result.duration == 11
