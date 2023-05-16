package com.github.marsrover;

public class MarsRover {
    private static final int GRID_SIZE_X = 10;
    private static final int GRID_SIZE_Y = 10;
    private Direction currentDirection;
    private int Y;
    private int X;

    public MarsRover() {
        currentDirection = Direction.NORTH;
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
                if (currentDirection.equals(Direction.NORTH)) {
                    this.Y += 1;
                }

                if (currentDirection.equals(Direction.WEST)) {
                    this.X -= 1;
                }

                if (currentDirection.equals(Direction.SOUTH)) {
                    this.Y -= 1;
                }

                if (currentDirection.equals(Direction.EAST)) {
                    this.X -= 1;
                }

                if (this.Y > GRID_SIZE_Y) {
                    this.Y = 0;
                }

                if (this.X > GRID_SIZE_X) {
                    this.X = 0;
                }
            }
        }

        return facing();
    }

    private String facing() {
        return String.format("%d:%d:%s", Math.abs(X), Math.abs(Y), currentDirection.value());
    }
}
