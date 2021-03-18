import pytest

import sys
sys.path.append('../')

from game_tennis.game.GAME import *

def create_game() -> Game:
    player1 = Player("AA", 0)
    player2 = Player("BB", 0)
    return Game(player1, player2)

def test_gameStart():
    #ARRANGE
    game = create_game()
    #ACT
    result = game.get_score()
    #ASSERT
    assert result == "Love-All"

def test_P1onePoint_ThenFifteenLove():
    #ARRANGE
    #game = create_game()
    player1 = Player("AA", 0)
    player2 = Player("BB", 0)
    Game(player1, player2)
    #ACT - Player 1 wins one point (1,0)
    Game.wins_point(player1)
    result = Game.get_score()
    #ASSERT+
    assert result == "Fifteen-Love"

def test_P1onePointAndP2onePoint_ThenThirtyLove():
    # ARRANGE
    game = create_game()
    # ACT - Player 1 and Player 2 wins 1 point (1,1)
    game.wins_point("Player1")
    game.wins_point("Player2")
    result = game.get_score()
    # ASSERT
    assert result == "Fifteen-All"

def test_P1onePointAndP2onePointAndP1twoPoints_thenThirtyLove():
    # ARRANGE
    game = create_game()
    # ACT - Player 1 and Player 2 wins 1 point and Player 1 win 2 points (2,1)
    game.wins_point("Player1")
    game.wins_point("Player2")
    game.wins_point("Player1")
    result = game.get_score()
    # ASSERT
    assert result == "Thirty-Love"