import random
from copy import deepcopy

from misc import find_length, calculate_orientation, find_first_pebble_of_given_type, check_game_won, check_n_formation, \
    find_length_n, check_open_ended_formation, check_formation_could_be_bigger


def computer_random_move(board):
    """
    Places a pebble on a random empty spot.
    """
    while True:
        i = random.randint(0,board.n()-1)
        j = random.randint(0,board.n()-1)
        try:
            if board.get_pebble_type(i,j) == -1:
                board.place_stone(1,i,j)
                return i,j  # just so i know where it moved
        except IndexError as ie:
            pass


def computer_move_at_row_end(board, orientation, x1, y1, x2, y2):
    """
    Attempts to place a pebble at the end of the sequence and return the pebble coords.
     If it can't, returns False
    """
    if orientation == 1:
        try:
            if board.get_pebble_type(x1, y1 - 1) == -1:
                board.place_stone(1, x1, y1 - 1)
                return x1, y1 - 1
        except IndexError as ie:
            pass
        try:
            if board.get_pebble_type(x2, y2 + 1) == -1:
                board.place_stone(1, x2, y2 + 1)
                return x2, y2 + 1
        except IndexError as ie:
            pass

    if orientation == 2:
        try:
            if board.get_pebble_type(x1 - 1, y1) == -1:
                board.place_stone(1, x1 - 1, y1)
                return x1 - 1, y1
        except IndexError as ie:
            pass
        try:
            if board.get_pebble_type(x2 + 1, y2) == -1:
                board.place_stone(1, x2 + 1, y2)
                return x2 + 1, y2
        except IndexError as ie:
            pass

    if orientation == 3:
        try:
            if board.get_pebble_type(x1 - 1, y1 - 1) == -1:
                board.place_stone(1, x1 - 1, y1 - 1)
                return x1 - 1, y1 - 1
        except IndexError as ie:
            pass
        try:
            if board.get_pebble_type(x2 + 1, y2 + 1) == -1:
                board.place_stone(1, x2 + 1, y2 + 1)
                return x2 + 1, y2 + 1
        except IndexError as ie:
            pass

    if orientation == 4:
        try:
            if board.get_pebble_type(x1 + 1, y1 - 1) == -1:
                board.place_stone(1, x1 + 1, y1 - 1)
                return x1 + 1, y1 - 1
        except IndexError as ie:
            pass
        try:
            if board.get_pebble_type(x2 - 1, y2 + 1) == -1:
                board.place_stone(1, x2 - 1, y2 + 1)
                return x2 - 1, y2 + 1
        except IndexError as ie:
            pass

    return False


def computer_move_around_xy(board, x, y):
    possible_directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)]
    random.shuffle(possible_directions)
    for item in possible_directions:
        try:
            if board.get_pebble_type(x+item[0], y+item[1]) == -1:
                board.place_stone(1, x+item[0], y+item[1])
                return x+item[0], y+item[1]
        except IndexError as ie:
            pass


def computer_check_n_formation_everywhere_around_xy(board, x, y, n):
    """
    Checks if AI placing a pebble around (x,y) would result in an n-formation.
    If so, returns True.
    """
    possible_directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)]
    for item in possible_directions:
        try:
            if board.get_pebble_type(x+item[0], y+item[1]) == -1:
                board.place_stone(1, x+item[0], y+item[1])
                if check_n_formation(board, x, y, n):
                    board.place_stone(-1, x + item[0], y + item[1])
                    return True
                board.place_stone(-1, x + item[0], y + item[1])
        except IndexError as ie:
            pass
    return False

# def computer_undo_everywhere_around_xy(board, x, y):
#     possible_directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)]
#     for item in possible_directions:
#         try:
#             if board.get_pebble_type(x+item[0], y+item[1]) == 1:
#                 board.place_stone(-1, x+item[0], y+item[1])
#         except IndexError as ie:
#             pass


def compute_next_offensive_move(board, x, y, length_limit=5):
    max_length = 0
    max_result = []
    for i in range(board.n()):
        for j in range(board.n()):
            if board.get_pebble_type(i, j) == 1:
                result = find_length(board, i, j)  # a list of tuples (m,[x1,y1], [x2,y2])
                length = result[0][0]
                if (length > max_length) and (length <= length_limit):
                    max_length = deepcopy(length)
                    max_result = deepcopy(result)

    print(max_result)

    for item in max_result:
        orientation = calculate_orientation(item[1], item[2])
        x1, y1 = item[1]
        x2, y2 = item[2]
        ai_move = computer_move_at_row_end(board, orientation, x1, y1, x2, y2)
        if ai_move:  # else: it just has to continue below
            return ai_move

    if length_limit == 1:  # if limit is 1 and this point was reached, there are no valid next moves so AI must try to go in another direction from its current pebbles
        for i in range(board.n()):
            for j in range(board.n()):
                if board.get_pebble_type(i, j) == 1:
                    return computer_move_around_xy(board, i, j)
        return computer_random_move(board)

    return compute_next_offensive_move(board, x, y, length_limit-1)

def offense_n(board, n):
    max_order = 0  # OFFENSE N IN ORDER OF IMPORTANCE
    max_ij = []
    for i in range(board.n()):
        for j in range(board.n()):
            if board.get_pebble_type(i, j) == -1:
                board.place_stone(1, i, j)
                order = 0
                for k in range(n, 6):
                    order += check_n_formation(board, i, j, k)

                if order > max_order:
                    board.place_stone(-1, i, j)  # to cancel the effect
                    max_order = deepcopy(order)
                    max_ij = deepcopy([i, j])
                else:
                    board.place_stone(-1, i, j)  # to cancel the effect
    if max_order:
        board.place_stone(1, max_ij[0], max_ij[1])
        return max_ij[0], max_ij[1]

def defense_n(board, n):
    max_order = 0  # DEFENSE AGAINST N IN ORDER OF IMPORTANCE
    max_ij = []
    for i in range(board.n()):
        for j in range(board.n()):
            if board.get_pebble_type(i, j) == -1:
                board.place_stone(0, i, j)
                order = 0
                for k in range(n, 6):
                    order += check_n_formation(board, i, j, k)

                if order > max_order:
                    board.place_stone(-1, i, j)  # to cancel the effect
                    max_order = deepcopy(order)
                    max_ij = deepcopy([i, j])
                else:
                    board.place_stone(-1, i, j)  # to cancel the effect
    if max_order:
        board.place_stone(1, max_ij[0], max_ij[1])
        return max_ij[0], max_ij[1]


def computer_calculated_move(board, x, y):
    """
    (x,y) is the pebble that has just been placed by the human.
    """
    #  FIRST COMPUTER MOVE
    computer_tiles_exist = False
    for i in range(board.n()):  # if there are no computer pebbles, AI must move at random.
        for j in range(board.n()):
            if board.get_pebble_type(i, j) == 1:
                computer_tiles_exist = True
    if not computer_tiles_exist:
        return computer_move_around_xy(board, x, y)
    # =================================================

    score_matrix = []
    human_open_formation_score_values = [0, 1, 6, 50, 121, 301, 301]  # ultima valoare ii dublata ca sa nu sara indexu inafara cand verifica daca ar putea fi mai mare
    human_closed_formation_score_values = [0, 1, 6, 26, 0, 301, 301]
    computer_open_formation_score_values = [0, 1, 5, 55, 140, 300, 300]
    computer_closed_formation_score_values = [0, 1, 5, 27, 0, 300, 300]

    for i in range(board.n()):
        score_matrix_new_row = []
        for j in range(board.n()):
            score_list = []
            score = 0
            """
            [[(m,[x1,y1],[x2,y2]), (m,[x1,y1],[x2,y2])], [(m,[x1,y1],[x2,y2])]]
            """
            if board.get_pebble_type(i, j) == -1: # DEFENSE CALCULATION
                board.place_stone(0, i, j)
                order = 0
                for k in range(6):
                    score_list.append(find_length_n(board, i, j, k))
                board.place_stone(-1, i, j)  # to cancel the effect
                """
                item: [(m,[x1,y1],[x2,y2]), (m,[x1,y1],[x2,y2])]
                subitem: (m,[x1,y1],[x2,y2])
                """
                for item in score_list:
                    for subitem in item:
                        if check_open_ended_formation(board, subitem):
                            # give more points
                            if check_formation_could_be_bigger(board, subitem) and (subitem[0] in [2,3]):
                                score += human_open_formation_score_values[subitem[0]+1]
                            else:
                                score += human_open_formation_score_values[subitem[0]]
                        else:
                            if check_formation_could_be_bigger(board, subitem):
                                score += human_closed_formation_score_values[subitem[0] + 1]
                            else:
                                score += human_closed_formation_score_values[subitem[0]]

            if board.get_pebble_type(i, j) == -1: # OFFENSE CALCULATION
                board.place_stone(1, i, j)
                order = 0
                for k in range(6):
                    score_list.append(find_length_n(board, i, j, k))
                board.place_stone(-1, i, j)  # to cancel the effect
                """
                item: [(m,[x1,y1],[x2,y2]), (m,[x1,y1],[x2,y2])]
                subitem: (m,[x1,y1],[x2,y2])
                """
                for item in score_list:
                    for subitem in item:
                        if check_open_ended_formation(board, subitem):
                            # give more points
                            if check_formation_could_be_bigger(board, subitem) and (subitem[0] in [2,3]):
                                score += computer_open_formation_score_values[subitem[0] + 1]
                            else:
                                score += computer_open_formation_score_values[subitem[0]]
                        else:
                            if check_formation_could_be_bigger(board, subitem):
                                score += computer_closed_formation_score_values[subitem[0] + 1]
                            else:
                                score += computer_closed_formation_score_values[subitem[0]]

            score_matrix_new_row.append(score)
        score_matrix.append(score_matrix_new_row)

    # for line in score_matrix:
    #     print(line)
    max_score = score_matrix[0][0]
    max_x = 0
    max_y = 0
    for i in range(board.n()):
        for j in range(board.n()):
            if score_matrix[i][j] > max_score:
                max_score = score_matrix[i][j]
                max_x = i
                max_y = j

    board.place_stone(1,max_x, max_y)
    return max_x, max_y

    # ===========================================


    # res = offense_n(board, 5)
    # if res:
    #     return res
    # res = defense_n(board, 5)
    # if res:
    #     return res
    # res = offense_n(board, 4)
    # if res:
    #     return res
    # res = defense_n(board, 4)
    # if res:
    #     return res
    # res = defense_n(board, 3)
    # if res:
    #     return res
    #
    # # Now it tries to think 1 move ahead, with a 3-FORMATION
    # possible_matrix_traversals = [1,2,3,4]
    # random.shuffle(possible_matrix_traversals)
    # opt = possible_matrix_traversals[0]
    # if opt == 1:
    #     for i in range(board.n()):
    #         for j in range(board.n()):
    #             if board.get_pebble_type(i, j) == -1:
    #                 board.place_stone(1, i, j)
    #                 if computer_check_n_formation_everywhere_around_xy(board, i, j, 3):
    #                     return i,j
    #                 board.place_stone(-1, i, j)  # to cancel the effect
    # if opt == 2:
    #     for i in range(board.n()):
    #         for j in reversed(range(j)):
    #             if board.get_pebble_type(i, j) == -1:
    #                 board.place_stone(1, i, j)
    #                 if computer_check_n_formation_everywhere_around_xy(board, i, j, 3):
    #                     return i,j
    #                 board.place_stone(-1, i, j)  # to cancel the effect
    # if opt == 3:
    #     for i in reversed(range(board.n())):
    #         for j in range(board.n()):
    #             if board.get_pebble_type(i, j) == -1:
    #                 board.place_stone(1, i, j)
    #                 if computer_check_n_formation_everywhere_around_xy(board, i, j, 3):
    #                     return i,j
    #                 board.place_stone(-1, i, j)  # to cancel the effect
    # if opt == 4:
    #     for i in reversed(range(board.n())):
    #         for j in reversed(range(board.n())):
    #             if board.get_pebble_type(i, j) == -1:
    #                 board.place_stone(1, i, j)
    #                 if computer_check_n_formation_everywhere_around_xy(board, i, j, 3):
    #                     return i,j
    #                 board.place_stone(-1, i, j)  # to cancel the effect
    #
    #
    # res = offense_n(board, 3)
    # if res:
    #     return res
    # res = offense_n(board, 2)
    # if res:
    #     return res
    # res = defense_n(board, 2)
    # if res:
    #     return res
    # return compute_next_offensive_move(board, x, y)



    # result = find_length(board, x, y)  # a list of tuples (m,[x1,y1], [x2,y2])
    # length = result[0][0]
    #
    # if length >= 3:
    #     for item in result:
    #         orientation = calculate_orientation(item[1], item[2])
    #         x1, y1 = item[1]
    #         x2, y2 = item[2]
    #         ai_move = computer_move_at_row_end(board, orientation, x1, y1, x2, y2)
    #         if ai_move:  # else: it just has to continue below
    #             return ai_move




    # for n in [5,4,3]:
    #     for i in range(board.n()):  # Attempts to place a tile to make an n-formation
    #         for j in range(board.n()):
    #             if board.get_pebble_type(i,j) == -1:
    #                 board.place_stone(1, i, j)
    #                 if check_n_formation(board, i,j, n):
    #                     return i,j
    #                 else:
    #                     board.place_stone(-1, i, j)  # to cancel the effect



    # possible_spot = [0,0]
    # while True:
    #     possible_spot = find_first_pebble_of_given_type(board, 1, possible_spot)
    #     if not possible_spot:
    #         return computer_random_move(board)
    #
    #     x = possible_spot[0]
    #     y = possible_spot[1]
    #     result = find_length(board, x, y)  # a list of tuples (m,[x1,y1], [x2,y2])
    #     length = result[0][0]
    #     for item in result:
    #         orientation = calculate_orientation(item[1], item[2])
    #         x1, y1 = item[1]
    #         x2, y2 = item[2]
    #         ai_move = computer_move_at_row_end(board, orientation, x1, y1, x2, y2)
    #         if ai_move:  # else: it has to try to go 1 tile in each orientation
    #             return ai_move
    #         else:
    #             result = []
    #             for i in range(5):
    #                 result.append((i, possible_spot, possible_spot))
    #
    #             for item in result:
    #                 orientation = calculate_orientation(item[1], item[2])
    #                 x1, y1 = item[1]
    #                 x2, y2 = item[2]
    #                 ai_move = computer_move_at_row_end(board, orientation, x1, y1, x2, y2)
    #                 if ai_move:
    #                     return ai_move
    #                 else:
    #                     return computer_random_move(board)












