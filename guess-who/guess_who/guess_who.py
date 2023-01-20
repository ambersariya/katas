class GuessWho:
    def __init__(self, character: str, game_characters: list) -> None:
        self.__turns = 0
        self.__characters = game_characters
        self.__game_character = self.__select_character(character)

    def guess(self, characteristic: str) -> set:
        self.__increment_turns()
        if characteristic == self.__game_character[0]:
            return {f"Correct! in {self.__turns} turns"}

        if not self.__matches_game_character(characteristic=characteristic):
            return self.__find_people_not_matching(characteristic=characteristic)
        return self.__find_people_matching(characteristic=characteristic)

    def __increment_turns(self):
        self.__turns += 1

    def __select_character(self, character: str) -> list:
        return [c for c in self.__characters if c[0] == character].pop()

    def __matches_game_character(self, characteristic: str) -> bool:
        game_character_name, game_character_qualities = self.__game_character
        return (characteristic == game_character_name) \
            or (characteristic in game_character_qualities)

    def __find_people_matching(self, characteristic: str) -> set:
        results = []
        for character in self.__characters:
            character_name, characteristics = character
            for _characteristic in characteristics:
                if characteristic == _characteristic or characteristic == character_name:
                    results.append(character_name)
        self.__reduce_game_characters(results)
        return set(results)

    def __find_people_not_matching(self, characteristic: str) -> set:
        results = []
        for character in self.__characters:
            character_name, character_qualities = character
            if characteristic not in character_qualities and characteristic not in character_name:
                results.append(character_name)
        self.__reduce_game_characters(results)
        return set(results)

    def __reduce_game_characters(self, exclusions: list):
        game_characters = self.__characters.copy()
        reduced_characters = [
            character for character in game_characters
            if character[0] in exclusions
        ]

        self.__characters = reduced_characters
