package com.github.marsrover;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class MarsRoverShould {
    @Test
    void face_north_at_the_start() {
        MarsRover marsRover = new MarsRover();
        assertEquals(marsRover.execute(""), "0:0:N");
    }
}