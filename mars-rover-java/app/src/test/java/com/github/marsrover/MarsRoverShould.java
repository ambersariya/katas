package com.github.marsrover;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

class MarsRoverShould {
    MarsRover marsRover;

    @BeforeEach
    public void setUp() {
        marsRover = new MarsRover();
    }

    @ParameterizedTest
    @CsvSource({
            "\"\", 0:0:N",
            "R,0:0:E",
            "RR,0:0:S",
            "RRR,0:0:W",
            "RRRR,0:0:N",
    })
    void execute_commands_to_turn_right(String input, String expected_output) {
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
        assertEquals(marsRover.execute(input), expected_output);
    }

    @ParameterizedTest
    @CsvSource({
            "M,0:1:N",
            "MM,0:2:N",
            "MMM,0:3:N",
            "MMMMMMMMMM,0:10:N",
            "MMMMMMMMMMM,0:0:N",
            "LM,1:0:W",
            "LLM,0:1:S",
            "LLLM,1:0:E",
            "RMR,1:0:S",
            "MMRMMLM,2:3:N",
    })
    void execute_commands_to_move_rover(String input, String expected_output) {
        assertEquals(expected_output, marsRover.execute(input));
    }
}
