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
                if (direction.equals("N")) {
                    direction = "E";
                    continue;
                }

                if (direction.equals("E")) {
                    direction = "S";
                    continue;
                }

                if (direction.equals("S")) {
                    direction = "W";
                    continue;
                }

                if (direction.equals("W")) {
                    direction = "N";
                }
            }
        }

        return "0:0:" + direction;
    }
}
