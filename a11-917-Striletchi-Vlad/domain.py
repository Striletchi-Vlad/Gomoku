from copy import deepcopy

import texttable


class Board:
    def __init__(self, n):
        """
        :param n: the size of the board
        """
        self.__matrix = []  # n*n matrix, will contain all the pebbles, -1 for none or 0/1 for the stone
        for i in range(n):
            self.__matrix.append([-1]*n)
        self.__n = n

    def n(self):
        return self.__n

    def get_pebble_type(self, x, y):
        if x<0 or y<0 or x>=self.__n or y>=self.__n:
            raise IndexError("Out of bounds.")
        return self.__matrix[x][y]

    def get_matrix(self):
        return self.__matrix

    def place_stone(self, type, x, y):
        self.__matrix[x][y] = type  # can be 0 for O, or 1 for X

    def __str__(self):
        result = texttable.Texttable()
        for i in range(self.__n):
            new_row = []
            for j in range(self.__n):
                if self.__matrix[i][j] == -1:
                    new_row.append(' ')
                if self.__matrix[i][j] == 0:
                    new_row.append('O')
                if self.__matrix[i][j] == 1:
                    new_row.append('X')
            result.add_row(new_row)
        return result.draw()

