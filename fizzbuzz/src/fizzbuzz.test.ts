import { describe, expect, test } from "@jest/globals";
// import { fizzbuzz } from "./fizzbuzz";

import { fizzbuzz } from "./fizzbuzz";

describe("fizzbuzz should", () => {
  test.each([
    [1, "1"],
    [2, "2"],
    [3, "Fizz"],
    [5, "Buzz"],
    [15, "FizzBuzz"],
    [75, "FizzBuzz"],
  ])("return %p given %p", (number: Number, result: String) => {
    expect(fizzbuzz(number)).toEqual(result);
  });
});
