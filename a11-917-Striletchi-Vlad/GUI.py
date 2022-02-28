import pygame

from AI import computer_calculated_move
from misc import check_game_won


bkg_colour = (0, 0, 77)
tile_size = 50
board_dimension = 15
border = 16
top_border = 100
display_width = tile_size * board_dimension + border * 2  # 782, for 15 tiles
display_height = tile_size * board_dimension + border + top_border # 866, for 15 tiles






class GraphicalMenu:
    def __init__(self, board):
        self.__board = board
        # self.matrix = self.__board.get_matrix()
        self.matrix_of_Tiles = []

        pygame.init()
        pygame.display.set_caption("G O M O K U")
        self.gameDisplay = pygame.display.set_mode((display_width, display_height))  # Create display
        self.clicks_allowed = True

        # Import files
        self.new_wallpaper = pygame.image.load("assets/new_wallpaper.png")
        self.tile_background = pygame.image.load("assets/pixil-frame-0 (3).png")
        self.empty_tile = pygame.image.load("assets/pixil-frame-0 (3).png")
        self.pink_tile = pygame.image.load("assets/pixil-frame-0 (5).png")
        self.purple_tile = pygame.image.load("assets/pixil-frame-0 (4).png")
        self.logo = pygame.image.load("assets/pixil-frame-0.png")
        self.win_message = pygame.image.load("assets/pixil-frame-0 (1).png")
        self.loss_message = pygame.image.load("assets/pixil-frame-0 (2).png")
        self.pebble_sound = pygame.mixer.Sound("assets/ui_tap-variant-01.wav")

    def start(self):

        # Generating entire grid
        for j in range(board_dimension):
            line = []
            for i in range(board_dimension):
                line.append(Tile(i, j, self.__board.get_pebble_type(i, j)))
            self.matrix_of_Tiles.append(line)

        self.gameDisplay.fill(bkg_colour)
        self.gameDisplay.blit(self.new_wallpaper, pygame.Rect(0,0,0,0))
        for i in self.matrix_of_Tiles:
            for j in i:
                j.draw_tile(self.gameDisplay, self.tile_background, self.pink_tile, self.purple_tile)
        self.gameDisplay.blit(self.logo, pygame.Rect(30, 0, 0 ,0))


        pygame.display.update()
        while True:


            for event in pygame.event.get():
                if self.clicks_allowed and event.type == pygame.MOUSEBUTTONUP:
                    for i in self.matrix_of_Tiles:
                        for j in i:
                            if j.rect.collidepoint(event.pos):
                                if event.button == 1:
                                    human_x = j.x
                                    human_y = j.y
                                    if self.__board.get_pebble_type(human_y, human_x) == -1:
                                        self.__board.place_stone(0, human_y, human_x)
                                        j.set_type(0)
                                        j.draw_tile(self.gameDisplay, self.empty_tile, self.pink_tile, self.purple_tile)
                                        pygame.mixer.Sound.play(self.pebble_sound)
                                        if check_game_won(self.__board, human_y, human_x):
                                            self.gameDisplay.blit(self.win_message, pygame.Rect(30, 0, 0, 0))
                                            pygame.display.update()
                                            self.clicks_allowed = False
                                            # return
                                        else:
                                            cx, cy = computer_calculated_move(self.__board, human_y, human_x)
                                            self.matrix_of_Tiles[cx][cy].set_type(1)
                                            self.matrix_of_Tiles[cx][cy].draw_tile(self.gameDisplay, self.empty_tile, self.pink_tile, self.purple_tile)

                                            if check_game_won(self.__board, cx, cy):
                                                self.gameDisplay.blit(self.loss_message, pygame.Rect(30, 0, 0, 0))
                                                self.clicks_allowed = False
                                                # return
                                        pygame.display.update()


class Tile:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.rect = pygame.Rect(border + self.x * tile_size, top_border + self.y * tile_size, tile_size,
                                tile_size)

    def set_type(self, value):
        self.type = value

    def draw_tile(self, display, empty_tile, pink_tile, purple_tile):
        if self.type == -1:
            display.blit(empty_tile, self.rect)
        if self.type == 0:
            display.blit(pink_tile, self.rect)
        if self.type == 1:
            display.blit(purple_tile, self.rect)