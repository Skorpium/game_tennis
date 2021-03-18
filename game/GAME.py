# This is a sample Python script.

class Game:

    def __init__(self, player1: str, player2: str):
        self._player1 = player1
        self._player2 = player2
        self._wins = ""

    def wins_point(self, player: str):
        self._wins = player

    def get_score(self) -> str:
        if self._wins == self._player1 :
            return "Fifteen-Love"
        if self._wins == self._player2:
            return "Fifteen-All"

        return "Love-All"

