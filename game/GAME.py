# This is a sample Python script.
class Player:

    def __init__(self, player: str, points: float):
        self._points = points
        self._player = player

    def add_points(self):
        self._points += 1

    def get_points(self):
        return self._points

    def get_name(self) -> str:
        return self._player

class Game:

    def __init__(self, p1: Player, p2: Player):
        self._player1 = p1
        self._player2 = p2

    def wins_point(self, player: Player):
        player.add_points()

    def get_score(self) -> str:
        if self._player1.get_points() == 0 == self._player2.get_points():
            return "Love-All"
        if 3 < self._player1.get_points() == self._player2.get_points() != 0:
            return "Deuce"

    def winner(self) -> str:
        if self._player1.get_points() == (self._player2.get_points()-2):
            return "Win for " + self._player1.get_name()
        if self._player2.get_points() == (self._player1.get_points()-2):
            return "Win for player 2"
    pass


