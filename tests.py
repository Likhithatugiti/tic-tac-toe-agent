import pytest
from game import TicTacToe

def test_win_conditions():
    game = TicTacToe()
    game.board = ['X','X','X',' ',' ',' ',' ',' ',' ']
    assert game.is_winner('X')

def test_available_moves():
    game = TicTacToe()
    assert len(game.available_moves()) == 9
    game.make_move(0, 'X')
    assert 0 not in game.available_moves()

def test_full_board():
    game = TicTacToe()
    for i in range(9):
        game.make_move(i, 'X')
    assert game.is_full()
