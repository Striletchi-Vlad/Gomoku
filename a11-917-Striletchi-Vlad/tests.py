import unittest

from domain import Board
from misc import check_game_won, find_length, calculate_orientation, find_first_pebble_of_given_type


class TestWinningCheck(unittest.TestCase):
    def setUp(self):
        self.my_board = Board(9)
        """
        +---+---+---+---+---+---+---+---+---+
        |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   |   |   | O | X |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   |   |   | O | O | X |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   |   |   | O | O | O |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   | X | X |   | O | O |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   | X |   |   |   |   |   |   | X |
        +---+---+---+---+---+---+---+---+---+
        |   |   |   |   | O |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   |   |   |   | X |   |   |   | O |
        +---+---+---+---+---+---+---+---+---+
        |   | X |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        """
        O_coords = [(1,3), (2,3), (2,4), (3,3), (3,4), (3,5), (4,4), (4,5), (6,4), (7,8)]
        X_coords = [(1,4), (2,5), (4,1), (4,2), (5,1), (5,8), (7,4), (8,1)]
        for item in O_coords:
            self.my_board.place_stone(0,item[0], item[1])
        for item in X_coords:
            self.my_board.place_stone(1,item[0], item[1])

    def testVerticalWin(self):
        self.my_board.place_stone(0, 5, 4)
        losing_coords = [(1,3), (2,3), (3,3), (3,5), (4,5), (7,8), (1,4), (2,5), (4,1), (4,2), (5,1), (5,8), (7,4), (8,1)]
        winning_coords = [(2,4), (3,4), (4,4), (5,4), (6,4)]

        for item in losing_coords:
            self.assertEqual(check_game_won(self.my_board, item[0], item[1]), False)
        for item in winning_coords:
            self.assertEqual(check_game_won(self.my_board, item[0], item[1]), True)

    def testHorizontalWin(self):
        self.my_board.place_stone(0, 3, 2)
        self.my_board.place_stone(0, 3, 6)
        losing_coords = [(1,3), (2,3), (4,5), (7,8), (1,4), (2,5), (4,1), (4,2), (5,1), (5,8), (7,4), (8,1), (2,4), (4,4), (6,4)]
        winning_coords = [(3,2), (3,3), (3,4), (3,5), (3,6)]

        for item in losing_coords:
            self.assertEqual(check_game_won(self.my_board, item[0], item[1]), False)
        for item in winning_coords:
            self.assertEqual(check_game_won(self.my_board, item[0], item[1]), True)

    def testMainDiagonalWin(self):
        self.my_board.place_stone(0, 0, 2)
        self.my_board.place_stone(0, 4, 6)
        losing_coords = [(2,3), (3,3), (4,5), (7,8), (1,4), (2,5), (4,1), (4,2), (5,1), (5,8), (7,4), (8,1), (3,4), (4,4), (6,4)]
        winning_coords = [(0,2), (4,6), (2,4), (3,5), (1,3)]

        for item in losing_coords:
            self.assertEqual(check_game_won(self.my_board, item[0], item[1]), False)
        for item in winning_coords:
            self.assertEqual(check_game_won(self.my_board, item[0], item[1]), True)

    def testSecondDiagonalWin(self):
        self.my_board.place_stone(0, 2, 6)
        self.my_board.place_stone(0, 5, 3)
        self.my_board.place_stone(0, 6, 2)
        losing_coords = [(2,3), (3,3), (4,5), (7,8), (1,4), (2,5), (4,1), (4,2), (5,1), (5,8), (7,4), (8,1), (3,4), (6,4)]
        winning_coords = [(3,5), (4,4), (2,6), (5,3), (6,2)]

        for item in losing_coords:
            self.assertEqual(check_game_won(self.my_board, item[0], item[1]), False)
        for item in winning_coords:
            self.assertEqual(check_game_won(self.my_board, item[0], item[1]), True)


class TestLengthCheck(unittest.TestCase):
    def setUp(self):
        self.my_board = Board(9)
        """
        +---+---+---+---+---+---+---+---+---+
        |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   |   |   | O | X |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   |   |   | O | O | X |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   |   |   | O | O | O |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   | X | X |   | O | O |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   | X |   |   |   |   |   |   | X |
        +---+---+---+---+---+---+---+---+---+
        |   |   |   |   | O |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   |   |   |   | X |   |   |   | O |
        +---+---+---+---+---+---+---+---+---+
        |   | X |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        """
        O_coords = [(1,3), (2,3), (2,4), (3,3), (3,4), (3,5), (4,4), (4,5), (6,4), (7,8)]
        X_coords = [(1,4), (2,5), (4,1), (4,2), (5,1), (5,8), (7,4), (8,1)]
        for item in O_coords:
            self.my_board.place_stone(0,item[0], item[1])
        for item in X_coords:
            self.my_board.place_stone(1,item[0], item[1])

    def testLength(self):
        self.assertEqual(find_length(self.my_board, 1, 3), [(3, [1,3], [3,3]), (3, [1,3], [3,5])])
        self.assertEqual(find_length(self.my_board, 2, 3), [(3, [1,3], [3,3]), (3, [2,3], [4,5])])
        self.assertEqual(find_length(self.my_board, 4, 1), [(2, [4,1], [4,2]), (2, [4,1], [5,1])])
        self.assertEqual(find_length(self.my_board, 7, 8), [(1, [7,8], [7,8]), (1, [7,8], [7,8]), (1, [7,8], [7,8]), (1, [7,8], [7,8]), (1, [7,8], [7,8])])
        self.assertEqual(find_length(self.my_board, 7, 4), [(1, [7,4], [7,4]), (1, [7,4], [7,4]), (1, [7,4], [7,4]), (1, [7,4], [7,4]), (1, [7,4], [7,4])])
        self.assertEqual(find_length(self.my_board, 1, 4), [(2, [1,4], [2,5])])


class TestCalculateOrientation(unittest.TestCase):
    def testOrientation(self):
        self.assertEqual(calculate_orientation([1,3], [1,6]), 1)
        self.assertEqual(calculate_orientation([1,3], [5,3]), 2)
        self.assertEqual(calculate_orientation([1,3], [3,5]), 3)
        self.assertEqual(calculate_orientation([2,3], [1,4]), 4)

class TestFindFirstPebble(unittest.TestCase):
    def setUp(self):
        self.my_board = Board(9)
        """
        +---+---+---+---+---+---+---+---+---+
        |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   |   |   | O | X |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   |   |   | O | O | X |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   |   |   | O | O | O |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   | X | X |   | O | O |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   | X |   |   |   |   |   |   | X |
        +---+---+---+---+---+---+---+---+---+
        |   |   |   |   | O |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   |   |   |   | X |   |   |   | O |
        +---+---+---+---+---+---+---+---+---+
        |   | X |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        """
        O_coords = [(1,3), (2,3), (2,4), (3,3), (3,4), (3,5), (4,4), (4,5), (6,4), (7,8)]
        X_coords = [(1,4), (2,5), (4,1), (4,2), (5,1), (5,8), (7,4), (8,1)]
        for item in O_coords:
            self.my_board.place_stone(0,item[0], item[1])
        for item in X_coords:
            self.my_board.place_stone(1,item[0], item[1])

    def testFind(self):
        self.assertEqual(find_first_pebble_of_given_type(self.my_board, 0), (1,3))
        self.assertEqual(find_first_pebble_of_given_type(self.my_board, 1), (1,4))
        self.assertEqual(find_first_pebble_of_given_type(self.my_board, 0, [3,6]), (4,4))
