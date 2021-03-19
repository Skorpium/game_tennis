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

def create_player(player: str) -> Player:
    return Player(player, 0)

def create_game() -> Game:
    player1 = create_player("AA")
    player2 = create_player("BB")
    return Game(player1, player2)

def test_gameStart():
    # ARRANGE
    game = create_game()

    # ACT
    result = game.get_score()

    # ASSERT
    assert result == "Love-All"

def test_onePlayerWinsOnePoint():
    # ARRANGE
    game = create_game()

    # ACT - Add one point to player
    player = Player("Alex", 5)
    game.wins_point(player)
    result = player.get_points()

    # ASSERT
    assert result == 6


