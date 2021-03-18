# This is a sample Python script.
class Player:

    def __init__(self, player: str, points: float):
        self._points = points
        self._player = player

    def add_points(self):
        self._points += 1
        return self._points

    def get_points(self):
        return self._points

class Game:

    def __init__(self, player1: Player, player2: Player):
        self._player1 = player1
        self._player2 = player2
        self._wins = ""

    @staticmethod
    def wins_point(self, player: Player):
        player.add_points()

    def get_score(self) -> str:
        if self._player1.get_points() == 1:
            return "Fifteen-Love"
        if self._wins == self._player2:
            return "Fifteen-All"

        return "Love-All"

