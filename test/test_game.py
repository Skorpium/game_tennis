import pytest
import sys
sys.path.append('../')
from game_tennis.game.GAME import *

@pytest.mark.parametrize("score_player1, score_player2, espected_result",
                         [(0, 0, "Love-All"),
                          (1, 1, "Fifteen-All"),
                          (0, 0, "Love-All"),
                          (1, 1, "Fifteen-All"),
                          (2, 2, "Thirty-All"),
                          (3, 3, "Deuce"),
                          (4, 4, "Deuce"),
                          (1, 0, "Fifteen-Love"),
                          (0, 1, "Love-Fifteen"),
                          (2, 0, "Thirty-Love"),
                          (0, 2, "Love-Thirty"),
                          (3, 0, "Forty-Love"),
                          (0, 3, "Love-Forty"),
                          (4, 0, "Win for player1"),
                          (0, 4, "Win for player2"),
                          (2, 1, "Thirty-Fifteen"),
                          (1, 2, "Fifteen-Thirty"),
                          (3, 1, "Forty-Fifteen"),
                          (1, 3, "Fifteen-Forty"),
                          (4, 1, "Win for player1"),
                          (1, 4, "Win for player2"),
                          (3, 2, "Forty-Thirty"),
                          (2, 3, "Thirty-Forty"),
                          (4, 2, "Win for player1"),
                          (2, 4, "Win for player2"),
                          (4, 3, "Advantage player1"),
                          (3, 4, "Advantage player2"),
                          (5, 4, "Advantage player1"),
                          (4, 5, "Advantage player2"),
                          (15, 14, "Advantage player1"),
                          (14, 15, "Advantage player2"),
                          (6, 4, "Win for player1"),
                          (4, 6, "Win for player2"),
                          (16, 14, "Win for player1"),
                          (14, 16, "Win for player2"), ])
def test_all(score_player1, score_player2, espected_result):
    return

@pytest.fixture()
def teardown():
    return

def create_player1(points: float, name: str) -> Player:
    return Player(name, points)

def create_player2(points: float, name: str) -> Player:
    return Player(name, points)

def create_game(p1_points: float, p2_points: float, p1_name: str, p2_name: str):
    p1 = create_player1(p1_points, p1_name)
    p2 = create_player2(p2_points, p1_name)
    return Game(p1, p2)

def test_gameStart():
    # ARRANGE
    game = create_game(0, 0, "Alex", "Ana")

    # ACT
    result = game.get_score()

    # ASSERT
    assert result == "Love-All"

def test_winner():
    # ARRANGE
    game = create_game(5, 3, "Alex", "Ona")

    # ACT - When one player win return "Win for player X"
    result = game.winner()

    # ASSERT
    assert result == "Win for " + game._player1.get_name()

def test_onePlayerWinsOnePoint():
    # ARRANGE
    game = create_game(5, 5, "Alex", "Ana")

    # ACT - Add one point to player
    game.wins_point(game.get_Player("Alex"))
    result = game.get_Player("Alex").get_points()

    # ASSERT
    assert result == 6
