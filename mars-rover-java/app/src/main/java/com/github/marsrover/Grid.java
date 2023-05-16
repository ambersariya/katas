package com.github.marsrover;

public class Grid {
    private static final int MAX_HEIGHT = 10;
    private static final int MAX_WIDTH = 10;

    public Coordinate next(Coordinate coordinate, Direction direction) {
        var x = coordinate.x();
        var y = coordinate.y();

        if (direction.equals(Direction.NORTH)) y += 1;
        if (direction.equals(Direction.SOUTH)) y -= 1;

        if (direction.equals(Direction.WEST)) x -= 1;
        if (direction.equals(Direction.EAST)) x += 1;

        if (y > MAX_HEIGHT) y = 0;
        if (x > MAX_WIDTH) x = 0;

        return new Coordinate(x, y);
    }
}