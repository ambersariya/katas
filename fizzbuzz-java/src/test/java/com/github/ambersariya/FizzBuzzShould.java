package com.github.ambersariya;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class FizzBuzzShould {
    @Test
    void return_string_1_when_given_1() {
        assertEquals("1", (new FizzBuzz()).fizzbuzz(1));
    }

    @Test
    void return_string_2_when_given_2() {
        assertEquals("2", (new FizzBuzz()).fizzbuzz(2));
    }
}