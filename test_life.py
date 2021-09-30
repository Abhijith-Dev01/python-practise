import pytest
import life_of_game
 
def test_rules():
    assert life_of_game.rules('*',3) == '*'
    assert life_of_game.rules('*',2) == '*'
    assert life_of_game.rules('*',7) == '-' 
    assert life_of_game.rules('*',1) == '-'
    assert life_of_game.rules('-',3) == '*'

def test_no_of_neighbour():
    assert life_of_game.no_of_neighbour(0,0,4,4) == 3
    assert life_of_game.no_of_neighbour(3,3,4,4) == 3
    assert life_of_game.no_of_neighbour(0,1,4,4) == 5
    assert life_of_game.no_of_neighbour(2,0,4,4) == 5
    assert life_of_game.no_of_neighbour(2,2,4,4) == 8