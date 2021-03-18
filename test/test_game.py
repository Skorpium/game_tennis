import pytest

import sys
sys.path.append('../')

from game_tennis.game.GAME import *

def test_callToGet_score():
    #ARRANGE
    #ACT
    get_score()

    #ASSERT
