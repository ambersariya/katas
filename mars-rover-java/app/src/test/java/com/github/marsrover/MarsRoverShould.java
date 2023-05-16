package com.github.marsrover;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

class MarsRoverShould {
    @ParameterizedTest
    @CsvSource({
            "\"\", 0:0:N",
            "R,0:0:E",
            "RR,0:0:S",
            "RRR,0:0:W",
            "RRRR,0:0:N",
    })
    void execute_commands_to_turn_right(String input, String expected_output) {
        MarsRover marsRover = new MarsRover();
        assertEquals(marsRover.execute(input), expected_output);
    }

    @ParameterizedTest
    @CsvSource({
            "\"\", 0:0:N",
            "L,0:0:W",
            "LL,0:0:S",
            "LLL,0:0:E",
            "LLLL,0:0:N",
    })
    void execute_commands_to_turn_left(String input, String expected_output) {
        MarsRover marsRover = new MarsRover();
        assertEquals(marsRover.execute(input), expected_output);
    }
}
