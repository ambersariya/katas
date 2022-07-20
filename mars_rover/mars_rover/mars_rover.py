from dataclasses import dataclass


@dataclass(init=True)
class Position:
    x: int
    y: int

    def __str__(self):
        return f"{self.x}:{self.y}"


class Direction:
    _directions = [
        'N', 'E', 'S', 'W'
    ]

    def __init__(self, facing: str):
        self._current_direction = self._directions.index(facing)

    def turn_right(self):
        self._current_direction += 1
        if self._current_direction >= len(self._directions):
            self._current_direction = 0

    def turn_left(self):
        self._current_direction -= 1
        if self._current_direction < 0:
            self._current_direction = len(self._directions) - 1

    def facing(self):
        return self._directions[self._current_direction]


class MarsRover:
    GRID_SIZE = 10

    _position: Position

    def __init__(self):
        self.direction = Direction(facing='N')
        self._position = Position(x=0, y=0)
        self._facing = 'N'

    def execute(self, command):
        if not command:
            return self.facing()

        for turn in command:
            if turn == 'R':
                self.direction.turn_right()
            if turn == 'L':
                self.direction.turn_left()
            if turn == 'M':
                self._move(self.direction.facing())

        return self.facing()

    def _move(self, facing: str):
        if facing == 'E':
            self._position.x += 1
        if facing == 'W':
            self._position.x -= 1
        if facing == 'S':
            self._position.y -= 1
        elif facing == 'N':
            self._position.y += 1

        if self._position.y % self.GRID_SIZE == 0:
            self._position.y = 0

        if self._position.x % self.GRID_SIZE == 0:
            self._position.x = 0

    def facing(self):
        return f'{self._position}:{self.direction.facing()}'
