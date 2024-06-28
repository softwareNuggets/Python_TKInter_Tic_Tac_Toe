import unittest
from unittest.mock import MagicMock
import tkinter as tk
from tic_tac_toe_pro import TicTacToe  # Replace with the actual file name

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.game = TicTacToe(self.root)
        
    def tearDown(self):
        self.root.destroy()


    def test_initialization(self):
        
        # Check if defaultFontName is 'Helvetica'
        self.assertEqual(self.game.defaultFontName, 'Helvetica')
        
        # Check if play_against_computer_var is an instance of tk.IntVar
        self.assertIsInstance(self.game.play_against_computer_var, tk.IntVar)


    def test_initial_state(self):
        self.assertFalse(self.game.game_over)
        self.assertEqual(self.game.my_win_count, 0)
        self.assertEqual(self.game.their_win_count, 0)
    
    def test_win_condition_row_err1(self):
        self.game.board = [['X', 'X', 'O'], ['', '', ''], ['', '', '']]
        self.assertTrue(self.game.check_win()==False)
        
    def test_win_condition_row_err2(self):
        self.game.board = [['X', '', 'O'], ['X', '', ''], ['O', '', 'X']]
        self.assertTrue(self.game.check_win()==False)
  
    def test_win_condition_row_err3(self):
        self.game.board = [['X', '', 'O'], ['X', '', 'O'], ['X', '', 'O']]
        self.assertTrue(self.game.check_win()==True)
  

    def test_win_condition_row_err4(self):
        self.game.board = [[' ', 'X', 'O'], ['X', 'X', 'O'], ['X', 'X', 'O']]
        self.assertTrue(self.game.check_win()==True)
        
    def test_win_condition_row_err5(self):
        self.game.board = [['X', 'O', 'O'], ['X', 'X', 'O'], ['0', 'X', ' ']]
        self.assertTrue(self.game.check_win()==False)  
    

    def test_win_condition_column(self):
        self.game.board = [['O', '', ''], ['O', '', ''], ['O', '', '']]
        self.assertTrue(self.game.check_win())

    def test_win_condition_diagonal(self):
        self.game.board = [['X', '', ''], ['', 'X', ''], ['', '', 'X']]
        self.assertTrue(self.game.check_win())

    def test_draw_condition(self):
        self.game.board = [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']]
        self.assertTrue(self.game.check_draw())

    def test_play_computer(self):
        self.game.play_against_computer_var = MagicMock(return_value=True)
        self.game.current_player = 'O'
        self.game.play_computer()
        # Check if computer made a move
        self.assertIn('O', [item for sublist in self.game.board for item in sublist])

    def test_restart(self):
        self.game.board = [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']]
        self.game.restart()
        self.assertEqual(self.game.board, [['', '', ''], ['', '', ''], ['', '', '']])
        self.assertFalse(self.game.game_over)


if __name__ == '__main__':
    unittest.main()
