export function fizzbuzz(number: Number) {
  const isDivisibleByThree: boolean = Number(number) % 3 == 0;
  const isDivisibleByFive: boolean = Number(number) % 5 == 0;
  if (isDivisibleByThree && isDivisibleByFive) return "FizzBuzz";
  if (isDivisibleByThree) return "Fizz";
  if (isDivisibleByFive) return "Buzz";
  return number.toString();
}
