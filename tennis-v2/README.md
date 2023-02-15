# Tennis

This kata is well suited to developers who have some familiarity with TDD basics and want to improve their algorithm
design skills. It is a stateless, algorithmic version of the classic Tennis kata (where the program also holds the
current score and updates its state when a player scores a new point).

Both Tennis and Bowling can also be done holding state (e.g. with a scorePoint() method of some sort). However, when
learning pure algorithmic TDD, we prefer to stay stateless as the added difficulty of maintaining state can distract
from the main learning points.

## Instructions

Write a program that accepts two integers, and converts them to a tennis-style score.

The scoring rules of tennis (per Wikipedia) are as follows:

- A game is won by the first player to have won at least four points in total and at least two points more than the
  opponent.
- Scores from zero to three points are described as “love”, “fifteen”, “thirty”, and “forty” respectively.
- If at least three points have been scored by each player and the scores are equal, the score is “deuce”.
- If at least three points have been scored by each player and a player has one more point than his opponent, the score
  is “advantage” for the player in the lead.

Start with the following interface:

```java
public class TennisScoreCalculator {
    public string Score(int player1Points, int player2Points);
}
```
