# Bank

link: [https://katalyst.codurance.com/bank](https://katalyst.codurance.com/bank)

When designing a big system, we like to base our design on the way that the system will be used.
That way, user stories
and acceptance criteria become much more than just a finish line: they are a guiding principle for
the entire system.

This solves a variety of problems. For example, it eliminates over-engineering (since we only write
what we know the
user needs). Starting at the public interface moves risk away from the end of the project (nobody
wants an integration
nightmare when deadline day is looming).

This Kata aims to distill that experience into a problem that can be knocked on the head in a couple
of hours, writing a
primitive bank account program. In this case, our user interface is just some public methods -
assume we're writing a
library. But the same principles hold.

It's a fantastic way to practice using acceptance tests to guide your design. If done correctly, the
result will be a
system that evolves itself with no extraneous effort and no nasty surprises at the end. You will see
how the outside-in
way of working can be a powerful way of creating object-oriented software.

You can attempt this using Mockist or Classicist TDD, but we find that it's especially well suited
to a Mockist
approach. Consider using Sandro Mancuso's screencast implementation as a reference.

Write a class named Account that implements the following public interface:

```java
public interface AccountService {
    void deposit(int amount);

    void withdraw(int amount);

    void printStatement();
}
```

> You cannot change the public interface of this class.

Here's the specification for an acceptance test that expresses the desired behaviour for this

```gherkin
# Scenario Print Statement
Given a client makes a deposit of 1000 on 10-01-2012
And a deposit of 2000 on 13-01-2012
And a withdrawal of 500 on 14-01-2012
When they print their bank statement
Then they would see:

Date       || Amount || Balance
14/01/2012 || -500   || 2500
13/01/2012 || 2000   || 3000
10/01/2012 || 1000   || 1000
```

We're using ints for the money amounts to keep the auxiliaries as simple as possible. In a real
system, we would always
use a datatype with guaranteed arbitrary precision, but doing so here would distract from the main
purpose of the
exercise.

Don't worry about spacing and indentation in the statement output. (You could instruct your
acceptance test to ignore
whitespace if you wanted to.)

Use the acceptance test to guide your progress towards the solution. Sandro does this by making all
unimplemented
methods throw an exception, so that he can immediately see what remains to be implemented when he
runs the acceptance
test.

When in doubt, go for the simplest solution!
