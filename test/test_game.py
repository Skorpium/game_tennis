import pytest

import sys
sys.path.append('../')

from game_tennis.game.GAME import *

def create_player(player: str) -> Player:
    return Player(player, 0)

def create_game() -> Game:
    player1 = create_player("AA")
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
    player1 = create_player("AA")
    player2 = create_player("BB")
    game = Game(player1, player2)

    #ACT - Player 1 wins one point (1,0)
    game.wins_point(player1)
    result = game.get_score()

    #ASSERT+
    assert result == "Fifteen-Love"

def test_P1onePointAndP2onePoint_ThenThirtyLove():
    # ARRANGE
    player1 = create_player("AA")
    player2 = create_player("BB")
    game = Game(player1, player2)

    # ACT - Player 1 and Player 2 wins 1 point (1,1)
    game.wins_point(player1)
    game.wins_point(player2)
    result = game.get_score()

    # ASSERT
    assert result == "Fifteen-All"

def test_P1onePointAndP2onePointAndP1twoPoints_thenThirtyLove():
    # ARRANGE
    player1 = create_player("AA")
    player2 = create_player("BB")
    game = Game(player1, player2)

    # ACT - Player 1 and Player 2 wins 1 point and Player 1 win 2 points (2,1)

    game.wins_point(player1)
    game.wins_point(player2)
    game.wins_point(player1)
    result = game.get_score()

    # ASSERT
    assert result == "Thirty-Love"