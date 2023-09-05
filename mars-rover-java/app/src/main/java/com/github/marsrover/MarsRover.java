package com.github.marsrover;

public class MarsRover {
    private Direction currentDirection;
    private Coordinate coordinates;
    private final Grid grid;

    public MarsRover() {
        currentDirection = Direction.NORTH;
        coordinates = new Coordinate(0, 0);
        grid = new Grid();
    }

    public String execute(String command) {
        for (char cmd : command.toCharArray()) {
            String singleCommand = String.valueOf(cmd);
            if (singleCommand.equals("R")) {
                currentDirection = currentDirection.turnRight();
            }

            if (singleCommand.equals("L")) {
                currentDirection = currentDirection.turnLeft();
            }

            if (singleCommand.equals("M")) {
                coordinates = grid.next(coordinates, currentDirection);
            }
        }

        return facing();
    }

    private String facing() {
        return String.format(
                "%d:%d:%s",
                coordinates.x(),
                coordinates.y(),
                currentDirection.value()
        );
    }
}
