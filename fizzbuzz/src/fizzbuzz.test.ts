import { describe, expect, test } from "@jest/globals";
// import { fizzbuzz } from "./fizzbuzz";

import { fizzbuzz } from "./fizzbuzz";

describe("fizzbuzz should", () => {
  test("return '1' when given 1", () => {
    expect(fizzbuzz(1)).toBe("1");
  });
  test("return '2' when given 2", () => {
    expect(fizzbuzz(2)).toBe("2");
  });
  test("return 'Fizz' when given 3", () => {
    expect(fizzbuzz(3)).toBe("Fizz");
  });
  test("return 'Buzz' when given 5", () => {
    expect(fizzbuzz(5)).toBe("Buzz");
  });
  test("return 'FizzBuzz' when given 15", () => {
    expect(fizzbuzz(15)).toBe("FizzBuzz");
  });
  test("return 'FizzBuzz' when given 75", () => {
    expect(fizzbuzz(75)).toBe("FizzBuzz");
  });
});
