import pytest
import life_of_game
 
def test_applt_rules():
    assert life_of_game.apply_rules('*',3) == '*'
    assert life_of_game.apply_rules('*',2) == '*'
    assert life_of_game.apply_rules('*',7) == '-' 
    assert life_of_game.apply_rules('*',1) == '-'
    assert life_of_game.apply_rules('-',3) == '*'

def test_neighbour_index():
    assert life_of_game.neighbour_index(0,0,5,5) == [[1,0],[1,1],[0,1]]
    assert life_of_game.neighbour_index(0,4,5,5) == [[1, 4], [1, 3], [0, 3]]
    assert life_of_game.neighbour_index(0,3,5,5) == [[0, 4], [1, 4], [1, 3], [1, 2], [0, 2]]
    assert life_of_game.neighbour_index(1,1,5,5) == [[0, 1], [0, 0], [0, 2], [2, 0], [2, 1], [2, 2], [1, 0], [1, 2]]
    assert life_of_game.neighbour_index(4,0,5,5) == [[3, 0], [3, 1], [4, 1]] 
    assert life_of_game.neighbour_index(2,0,5,5) == [[1, 0], [3, 0], [3, 1], [1, 1], [2, 1]]
    assert life_of_game.neighbour_index(4,4,5,5) == [[3, 4], [3, 3], [4, 3]]
    assert life_of_game.neighbour_index(4,3,5,5) == [[3, 3], [4, 2], [4, 4], [3, 4], [3, 2]] 
    assert life_of_game.neighbour_index(2,4,5,5) == [[1, 4], [3, 4], [3, 3], [1, 3], [2, 3]]  


def test_no_of_neighbour():
    arr = [['-','-','-','-','-'],
            ['-','-','*','-','-'],
            ['-','-','*','-','-'],
            ['-','-','*','-','-'],
            ['-','-','-','-','-']]
    assert life_of_game.no_of_neighbour([[1, 0], [1, 1], [0, 1]],arr) == 0
    assert life_of_game.no_of_neighbour([[0, 1], [0, 0], [0, 2], [2, 0], 
                                        [2, 1], [2, 2], [1, 0], [1, 2]],arr) == 2
    assert life_of_game.no_of_neighbour([[0, 4], [1, 4], [1, 3], [1, 2], 
                                        [0, 2]],arr) == 1
    assert life_of_game.no_of_neighbour([[1, 3], [1, 2], [1, 4], [3, 2], 
                                        [3, 3], [3, 4], [2, 2], [2, 4]],arr) == 3
