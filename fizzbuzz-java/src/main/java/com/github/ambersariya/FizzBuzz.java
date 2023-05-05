package com.github.ambersariya;

public class FizzBuzz {
    public String convert(int number) {
        boolean multipleOfThree = number % 3 == 0;
        boolean multipleOfFive = number % 5 == 0;

        if (multipleOfFive && multipleOfThree){
            return "FizzBuzz";
        }

        if (multipleOfThree) {
            return "Fizz";
        }
        if (multipleOfFive) {
            return "Buzz";
        }

        return String.valueOf(number);
    }
}
