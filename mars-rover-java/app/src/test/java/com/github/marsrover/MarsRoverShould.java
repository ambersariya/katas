package com.github.marsrover;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

class MarsRoverShould {
    @ParameterizedTest
    @CsvSource({"\"\", 0:0:N", "R,0:0:E", "RR,0:0:S"})
    void execute_commands(String input, String expected_output) {
        MarsRover marsRover = new MarsRover();
        assertEquals(marsRover.execute(input), expected_output);
    }
}

// add slide around pairing styles
//