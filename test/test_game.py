import pytest

import sys
sys.path.append('../')

from game_tennis.game.GAME import *

def test_gameStart():
    #ARRANGE
    #ACT
    result = get_score()

    #ASSERT
    assert result == "Love-All"
