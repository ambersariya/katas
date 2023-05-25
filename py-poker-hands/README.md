# Poker Hands

Compare two Poker Hands and decide which wins. A Poker hand comprises 5 cards dealt from a normal 52 card deck, and each card has a suit and a value.

All suits have the same rank, for example the Ace of Clubs is not beaten by the Ace of Spades, they are equal.

A poker hand can be represented using symbols like this:

```text
2H 3D 5S 9C KD
```

(Two of Hearts, 3 of Diamonds, 5 of Spades, 9 of Clubs, King of Diamonds)

The suit of the card is represented by one character:

| Clubs | Diamonds | Hearts | Spades |
| ----- | -------- | ------ | ------ |
|   C   |     D    |    H   |    S   |

The face value of the card is represented by another character, either the number on the face, or one of the following special cases:


| 10 | Jack | Queen | King | Ace |
|----| ---- | ----- | ---- | --- |
|  T |   J  |   Q   |   K  |  A  |

You compare Poker hands by deciding which has the higher rank, according to the categories below.

These categories are listed in order of ascending rank. For example, a hand containing a Full House has higher rank than a hand containing a Pair.

- **High Card**: The value of the highest card in the hand. If the highest cards have the same value, the hands are ranked by the next highest, and so on.
- **Pair**: 2 of the 5 cards in the hand have the same value. Hands which both contain a pair are ranked by the value of the cards forming the pair. If these values are the same, the hands are ranked by the values of the cards not forming the pair, in decreasing order.
- **Two Pairs**: The hand contains 2 different pairs. Hands which both contain 2 pairs are ranked by the value of their highest pair. Hands with the same highest pair are ranked by the value of their other pair. If these values are the same the hands are ranked by the value of the remaining card.
- **Three of a Kind**: Three of the cards in the hand have the same value. Hands which both contain three of a kind are ranked by the value of the 3 cards.
- **Straight**: Hand contains 5 cards with consecutive val- ues. Hands which both contain a straight are ranked by their highest card.
- **Flush**: Hand contains 5 cards of the same suit. Hands which are both flushes are ranked using the rules for High Card.
- **FullHouse**: 3 cards of the same value,with the remaining 2 cards forming a pair. Ranked by the value of the 3 cards.
- **Four of a kind**: 4 cards with the same value.Ranked by the value of the 4 cards.
- **Straight flush**: 5 cards of the same suit with consecutive values. Ranked by the highest card in the hand.

If you like, you can read the two hands to be compared from standard input, and write which won to standard output:

```bash

2H 3D 5S 9C KD 
2C 3H 4S 8C AH

Player 2 wins.

```

## Additional discussion points for the retrospective:

- How did you choose the order of test cases to implement?

- Are all your tests for whole hands?Or do you have tests for comparing smaller numbers of cards?

## Ideas for after the Dojo

Try this Kata in the London School style of TDD, (or the classic style if you already did it like that).