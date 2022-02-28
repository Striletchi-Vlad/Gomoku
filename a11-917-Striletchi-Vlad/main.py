# G O M O K U
from GUI import GraphicalMenu
from console_ui import ConsoleMenu
from domain import Board

my_board = Board(15)
my_console = GraphicalMenu(my_board)
my_console.start()



#TODO only some very slight weight calibrations
#TODO check for full board (tie)