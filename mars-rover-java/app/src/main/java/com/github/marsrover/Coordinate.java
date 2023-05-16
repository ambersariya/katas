package com.github.marsrover;

public class Coordinate {
    private final int x;
    private final int y;

    public Coordinate(int x, int y) {
        this.x = Math.abs(x);
        this.y = Math.abs(y);
    }

    public int x() {
        return x;
    }

    public int y() {
        return y;
    }
}
