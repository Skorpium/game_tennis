import pytest

import sys
sys.path.append('../')

from game_tennis.game.GAME import *

def create_game() -> Game:
    return Game("Player1", "Player2")

def test_gameStart():
    #ARRANGE
    game = create_game()
    #ACT
    result = game.get_score()

    #ASSERT
    assert result == "Love-All"

def test_P1onePoint_ThenFifteenLove():
    #ARRANGE
    game = create_game()
    #ACT - Player 1 wins one point
    game.wins_point("Player1")
    result = game.get_score()

    #ASSERT
    assert result == "Fifteen-Love"
