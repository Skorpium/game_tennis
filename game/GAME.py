# This is a sample Python script.
import sys
from game_tennis.Player.Player import Player

class Game:
    def __init__(self, p1: Player, p2: Player):
        self._player1 = p1
        self._player2 = p2

    def wins_point(self, p: Player):
        p.add_points()

    def get_score(self) -> str:
        if self._player1.get_points() == 0 == self._player2.get_points():
            return "Love-All"
        if 3 < self._player1.get_points() == self._player2.get_points() != 0:
            return "Deuce"

    def winner(self):
        if self._player1.get_points() == (self._player2.get_points()-2):
            return "Win for " + self._player1.get_name()
        if self._player2.get_points() == (self._player1.get_points()-2):
            return "Win for " + self._player2.get_name()

        return "fail"

    def get_Player(self, name: str) -> Player:
        if self._player1.get_name() == name:
            return self._player1
        if self._player2.get_name() == name:
            return self._player2

