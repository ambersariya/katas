package com.github.marsrover;

public class MarsRover {
    private String direction;

    public MarsRover() {
        direction = "N";
    }

    public String execute(String command) {
        return "0:0:" + direction;
    }
}
