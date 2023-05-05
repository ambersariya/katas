package com.github.ambersariya;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.ValueSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

class FizzBuzzShould {

    FizzBuzz fizzBuzz;

    @BeforeEach
    void setup(){
        fizzBuzz = new FizzBuzz();
    }

    @ParameterizedTest
    @CsvSource({"1,1", "2,2", "3,Fizz", "6,Fizz", "5,Buzz", "15,FizzBuzz"})
    void return_string_when_given_input(int input, String expected){
        assertEquals(expected, fizzBuzz.convert(input));
    }
}