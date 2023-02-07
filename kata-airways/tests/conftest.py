import pytest

from src.core.route_map import RouteMap
from src.core.value_objects import Route, Airport


@pytest.fixture
def allowed_routes():
    return [
        Route(Airport('LHR'), Airport('LAX'), 11),
        Route(Airport('LAX'), Airport('LHR'), 11),

        Route(Airport('LHR'), Airport('JFK'), 8),
        Route(Airport('JFK'), Airport('LHR'), 8),

        Route(Airport('LHR'), Airport('BER'), 1.8),
        Route(Airport('BER'), Airport('LHR'), 1.8),

        Route(Airport('LHR'), Airport('ATH'), 3),
        Route(Airport('ATH'), Airport('LHR'), 3),

        Route(Airport('LHR'), Airport('CDG'), 1),
        Route(Airport('CDG'), Airport('LHR'), 1),

        Route(Airport('LHR'), Airport('DUB'), 1),
        Route(Airport('DUB'), Airport('LHR'), 1),

        Route(Airport('LHR'), Airport('MXP'), 2),
        Route(Airport('MXP'), Airport('LHR'), 2),

        Route(Airport('LHR'), Airport('DXB'), 7),
        Route(Airport('DXB'), Airport('LHR'), 7),
    ]


@pytest.fixture
def route_map(allowed_routes):
    return RouteMap(allowed_routes=allowed_routes)