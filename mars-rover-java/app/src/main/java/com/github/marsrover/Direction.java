package com.github.marsrover;

public enum Direction {
    NORTH("N", "W", "E"),
    WEST("W", "S", "N"),
    SOUTH("S", "E", "W"),
    EAST("E", "N", "S");

    private final String left;
    private final String value;
    private final String right;

    Direction(String value, String left, String right) {
        this.value = value;
        this.left = left;
        this.right = right;
    }

    public Direction turnRight() {
        return directionTo(this.right);
    }

    public Direction turnLeft() {
        return directionTo(this.left);
    }

    public String value() {
        return value;
    }

    private Direction directionTo(String value) {
        for (var direction : values()) {
            if (direction.value.equals(value)) {
                return direction;
            }
        }
        return null;
    }
}