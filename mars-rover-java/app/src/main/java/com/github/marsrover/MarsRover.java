package com.github.marsrover;

public class MarsRover {
    private String direction;

    public MarsRover() {
        direction = "N";
    }

    public String execute(String command) {
        for (char cmd : command.toCharArray()) {
            String singleCommand = String.valueOf(cmd);
            if (singleCommand.equals("R")) {
                direction = turnRight();
            }

            if (singleCommand.equals("L")) {
                direction = turnLeft();
            }
        }

        return "0:0:" + direction;
    }

    private String turnLeft() {
        if (direction.equals("N")) {
            return "W";
        }

        if (direction.equals("W")) {
            return "S";
        }

        if (direction.equals("S")) {
            return "E";
        }

        return "N";
    }

    private String turnRight() {
        if (direction.equals("N")) {
            return "E";
        }

        if (direction.equals("E")) {
            return "S";
        }

        if (direction.equals("S")) {
            return "W";
        }

        return "N";
    }
}
