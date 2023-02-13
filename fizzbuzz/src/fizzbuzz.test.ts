import { describe, expect, test } from "@jest/globals";

describe("fizzbuzz should", () => {
  test("return '1' when given 1", () => {
    expect(fizzbuzz(1)).toBe("1");
  });
});
