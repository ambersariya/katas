import dataclasses
from typing import Optional

from src.core.errors import UnknownDestination
from src.core.value_objects import Route, make_route_key


@dataclasses.dataclass()
class RouteMap:
    def __init__(self, allowed_routes: list[Route]):
        self.__allowed_routes = self.__create_indexable_map(allowed_routes)

    @staticmethod
    def __create_indexable_map(allowed_routes: list[Route]) -> dict[str, Route]:
        return {f'{route.id()}': route for route in allowed_routes}

    def is_valid_route(self, origin: str, destination: str) -> bool:
        return make_route_key(origin, destination) in self.__allowed_routes

    def get_route(self, origin, destination) -> Optional[Route]:
        if not self.is_valid_route(origin=origin, destination=destination):
            raise UnknownDestination()
        return self.__allowed_routes[make_route_key(origin, destination)]
