package com.github.marsrover;

public class MarsRover {
    private Direction currentDirection;

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
        }

        return "0:0:" + currentDirection.value();
    }
}
