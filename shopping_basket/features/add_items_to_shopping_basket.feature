Feature: add items to shopping basket

    Scenario: prints contents of the basket

        Given I add "2" units of "The Hobbit" to my shopping basket
        And I add "5" units of "Breaking Bad"
        When I check the content of my shopping basket
        Then it should contain the following information:
        """
        Creation date (of the shopping basket)
        2 x The Hobbit // 2 x 5.00 = £10.00
        5 x Breaking Bad // 5 x 7.00 = £35.00
        Total: £45.00
        """
