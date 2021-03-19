# This is a sample Python script.
class Player:

    def __init__(self, player: str, points: float):
        self._points = points
        self._player = player

    def add_points(self):
        self._points += 1

    def get_points(self):
        return self._points

class Game:

    def __init__(self, p1: Player, p2: Player):
        self._player1 = p1
        self._player2 = p2
    #    self._wins = ""

    def wins_point(self, player: Player):
        player.add_points()

    def get_score(self) -> str:
        if self._player1.get_points() == 1 & (self._player2.get_points() == 0):
            return "Fifteen-Love"
        if self._player1.get_points() == 1 == self._player2.get_points():
            return "Fifteen-All"
        if (self._player1.get_points() == 2) & (self._player2.get_points() == 1):
            return "Thirty-Love"

        return "Love-All"
