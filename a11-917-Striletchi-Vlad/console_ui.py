from AI import computer_random_move, computer_calculated_move
from misc import check_game_won


class ConsoleMenu:
    def __init__(self, board):
        self.__board = board

    def start(self):
        while True:
            print(str(self.__board))
            x = int(input("give x: "))
            y = int(input("give y: "))
            self.__board.place_stone(0,x,y)
            if check_game_won(self.__board, x, y):
                print("You won!")
                return
            cx, cy = computer_calculated_move(self.__board, x, y)
            if check_game_won(self.__board, cx, cy):
                print("Computer wins.")
                return
