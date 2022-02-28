def check_n_formation(board,x,y,n=5):
    """
    Checks if placing a tile on (x,y) resulted in a row of 5.
    """
    pebble_type = board.get_pebble_type(x,y)
    counter = 0

    # Horizontal check ================================================================
    consecutive_pebbles = 1
    next_tile_to_check = [x, y]
    ## Left
    while next_tile_to_check[1] - 1 >= 0:  # = left border not reached
        next_tile_to_check[1] -= 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            if consecutive_pebbles == n:
                counter += 1
        else:
            break

    ## Right
    next_tile_to_check = [x, y]
    while next_tile_to_check[1] + 1 < board.n():  # = right border not reached
        next_tile_to_check[1] += 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            if consecutive_pebbles == n:
                counter += 1
        else:
            break

    # Vertical check ==================================================================
    consecutive_pebbles = 1
    next_tile_to_check = [x,y]
    ## Up
    while next_tile_to_check[0]-1 >= 0: # = Lower border not reached
        next_tile_to_check[0] -= 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            if consecutive_pebbles == n:
                counter += 1
        else:
            break

    ## Down
    next_tile_to_check = [x, y]
    while next_tile_to_check[0]+1 < board.n():  # = Upper border not reached
        next_tile_to_check[0] += 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            if consecutive_pebbles == n:
                counter += 1
        else:
            break

    # Main diagonal check ==================================================================
    consecutive_pebbles = 1
    next_tile_to_check = [x,y]
    ## Up & left
    while (next_tile_to_check[0]-1 >= 0) and (next_tile_to_check[1]-1 >= 0): # = Upper corner not reached
        next_tile_to_check[0] -= 1
        next_tile_to_check[1] -= 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            if consecutive_pebbles == n:
                counter += 1
        else:
            break

    ## Down & right
    next_tile_to_check = [x, y]
    while (next_tile_to_check[0]+1 < board.n()) and (next_tile_to_check[1]+1 < board.n()):  # = Lower corner not reached
        next_tile_to_check[0] += 1
        next_tile_to_check[1] += 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            if consecutive_pebbles == n:
                counter += 1
        else:
            break

    # Secondary diagonal check ==================================================================
    consecutive_pebbles = 1
    next_tile_to_check = [x, y]
    ## Up & right
    while (next_tile_to_check[0]-1 >= 0) and (next_tile_to_check[1]+1 < board.n()):  # = Upper corner not reached
        next_tile_to_check[0] -= 1
        next_tile_to_check[1] += 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            if consecutive_pebbles == n:
                counter += 1
        else:
            break

    ## Down & left
    next_tile_to_check = [x, y]
    while (next_tile_to_check[0]+1 < board.n()) and (next_tile_to_check[1]-1 >= 0):  # = Lower corner not reached
        next_tile_to_check[0] += 1
        next_tile_to_check[1] -= 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            if consecutive_pebbles == n:
                counter += 1
        else:
            break

    return counter

def check_game_won(board,x,y):
    """
    Checks if placing a tile on (x,y) resulted in a row of 5.
    """
    pebble_type = board.get_pebble_type(x,y)

    # Horizontal check ================================================================
    consecutive_pebbles = 1
    next_tile_to_check = [x, y]
    ## Left
    while next_tile_to_check[1] - 1 >= 0:  # = left border not reached
        next_tile_to_check[1] -= 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            if consecutive_pebbles == 5:
                return True
        else:
            break

    ## Right
    next_tile_to_check = [x, y]
    while next_tile_to_check[1] + 1 < board.n():  # = right border not reached
        next_tile_to_check[1] += 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            if consecutive_pebbles == 5:
                return True
        else:
            break

    # Vertical check ==================================================================
    consecutive_pebbles = 1
    next_tile_to_check = [x,y]
    ## Up
    while next_tile_to_check[0]-1 >= 0: # = Lower border not reached
        next_tile_to_check[0] -= 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            if consecutive_pebbles == 5:
                return True
        else:
            break

    ## Down
    next_tile_to_check = [x, y]
    while next_tile_to_check[0]+1 < board.n():  # = Upper border not reached
        next_tile_to_check[0] += 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            if consecutive_pebbles == 5:
                return True
        else:
            break

    # Main diagonal check ==================================================================
    consecutive_pebbles = 1
    next_tile_to_check = [x,y]
    ## Up & left
    while (next_tile_to_check[0]-1 >= 0) and (next_tile_to_check[1]-1 >= 0): # = Upper corner not reached
        next_tile_to_check[0] -= 1
        next_tile_to_check[1] -= 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            if consecutive_pebbles == 5:
                return True
        else:
            break

    ## Down & right
    next_tile_to_check = [x, y]
    while (next_tile_to_check[0]+1 < board.n()) and (next_tile_to_check[1]+1 < board.n()):  # = Lower corner not reached
        next_tile_to_check[0] += 1
        next_tile_to_check[1] += 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            if consecutive_pebbles == 5:
                return True
        else:
            break

    # Secondary diagonal check ==================================================================
    consecutive_pebbles = 1
    next_tile_to_check = [x, y]
    ## Up & right
    while (next_tile_to_check[0]-1 >= 0) and (next_tile_to_check[1]+1 < board.n()):  # = Upper corner not reached
        next_tile_to_check[0] -= 1
        next_tile_to_check[1] += 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            if consecutive_pebbles == 5:
                return True
        else:
            break

    ## Down & left
    next_tile_to_check = [x, y]
    while (next_tile_to_check[0]+1 < board.n()) and (next_tile_to_check[1]-1 >= 0):  # = Lower corner not reached
        next_tile_to_check[0] += 1
        next_tile_to_check[1] -= 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            if consecutive_pebbles == 5:
                return True
        else:
            break

    return False

def find_length(board, x,y):
    """
    Returns a list of tuples (m,[x1,y1],[x2,y2]), where:
        - m is the maximum length of the sequence containing the pebble (x,y)
        - (x1, y1) is the start of the sequence
        - (x2, y2) is the end of the sequence
    """
    pebble_type = board.get_pebble_type(x,y)
    max_length = 1
    max_start = [x,y]
    max_end = [x,y]
    result = [(max_length, max_start, max_end)]

    # Horizontal check ================================================================
    consecutive_pebbles = 1
    next_tile_to_check = [x, y]
    curr_length = 1
    curr_start = [x,y]
    curr_end = [x,y]

    ## Left
    while next_tile_to_check[1] - 1 >= 0:  # = left border not reached
        next_tile_to_check[1] -= 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            curr_start[1] -= 1
            curr_length += 1
        else:
            break

    ## Right
    next_tile_to_check = [x, y]
    while next_tile_to_check[1] + 1 < board.n():  # = right border not reached
        next_tile_to_check[1] += 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            curr_end[1] += 1
            curr_length += 1
        else:
            break

    if curr_length == max_length:
        result.append((curr_length, curr_start, curr_end))
    if curr_length > max_length:
        max_length = curr_length
        max_start = curr_start
        max_end = curr_end
        result = [(max_length, max_start, max_end)]

    # Vertical check ==================================================================
    consecutive_pebbles = 1
    next_tile_to_check = [x,y]
    curr_length = 1
    curr_start = [x, y]
    curr_end = [x, y]

    ## Up
    while next_tile_to_check[0]-1 >= 0: # = Lower border not reached
        next_tile_to_check[0] -= 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            curr_start[0] -= 1
            curr_length += 1
        else:
            break

    ## Down
    next_tile_to_check = [x, y]
    while next_tile_to_check[0]+1 < board.n():  # = Upper border not reached
        next_tile_to_check[0] += 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            curr_end[0] += 1
            curr_length += 1
        else:
            break

    if curr_length == max_length:
        result.append((curr_length, curr_start, curr_end))
    if curr_length > max_length:
        max_length = curr_length
        max_start = curr_start
        max_end = curr_end
        result = [(max_length, max_start, max_end)]

    # Main diagonal check ==================================================================
    consecutive_pebbles = 1
    next_tile_to_check = [x,y]
    curr_length = 1
    curr_start = [x, y]
    curr_end = [x, y]

    ## Up & left
    while (next_tile_to_check[0]-1 >= 0) and (next_tile_to_check[1]-1 >= 0): # = Upper corner not reached
        next_tile_to_check[0] -= 1
        next_tile_to_check[1] -= 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            curr_start[0] -= 1
            curr_start[1] -= 1
            curr_length += 1
        else:
            break

    ## Down & right
    next_tile_to_check = [x, y]
    while (next_tile_to_check[0]+1 < board.n()) and (next_tile_to_check[1]+1 < board.n()):  # = Lower corner not reached
        next_tile_to_check[0] += 1
        next_tile_to_check[1] += 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            curr_end[0] += 1
            curr_end[1] += 1
            curr_length += 1
        else:
            break

    if curr_length == max_length:
        result.append((curr_length, curr_start, curr_end))
    if curr_length > max_length:
        max_length = curr_length
        max_start = curr_start
        max_end = curr_end
        result = [(max_length, max_start, max_end)]

    # Secondary diagonal check ==================================================================
    consecutive_pebbles = 1
    next_tile_to_check = [x, y]
    curr_length = 1
    curr_start = [x, y]
    curr_end = [x, y]

    ## Up & right
    while (next_tile_to_check[0]-1 >= 0) and (next_tile_to_check[1]+1 < board.n()):  # = Upper corner not reached
        next_tile_to_check[0] -= 1
        next_tile_to_check[1] += 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            curr_end[0] -= 1
            curr_end[1] += 1
            curr_length += 1
        else:
            break

    ## Down & left
    next_tile_to_check = [x, y]
    while (next_tile_to_check[0]+1 < board.n()) and (next_tile_to_check[1]-1 >= 0):  # = Lower corner not reached
        next_tile_to_check[0] += 1
        next_tile_to_check[1] -= 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            curr_start[0] += 1
            curr_start[1] -= 1
            curr_length += 1
        else:
            break

    if curr_length == max_length:
        result.append((curr_length, curr_start, curr_end))
    if curr_length > max_length:
        max_length = curr_length
        max_start = curr_start
        max_end = curr_end
        result = [(max_length, max_start, max_end)]

    return result


def find_length_n(board, x, y, n):
    """
    Returns a list of tuples (m,[x1,y1],[x2,y2]), where:
        - m is the length(=n) of the sequence containing the pebble (x,y)
        - (x1, y1) is the start of the sequence
        - (x2, y2) is the end of the sequence
    """
    pebble_type = board.get_pebble_type(x,y)
    max_length = 1
    max_start = [x,y]
    max_end = [x,y]
    result = [(max_length, max_start, max_end)]

    # Horizontal check ================================================================
    consecutive_pebbles = 1
    next_tile_to_check = [x, y]
    curr_length = 1
    curr_start = [x,y]
    curr_end = [x,y]

    ## Left
    while next_tile_to_check[1] - 1 >= 0:  # = left border not reached
        next_tile_to_check[1] -= 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            curr_start[1] -= 1
            curr_length += 1
        else:
            break

    ## Right
    next_tile_to_check = [x, y]
    while next_tile_to_check[1] + 1 < board.n():  # = right border not reached
        next_tile_to_check[1] += 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            curr_end[1] += 1
            curr_length += 1
        else:
            break

    if curr_length == n:
        result.append((curr_length, curr_start, curr_end))

    # Vertical check ==================================================================
    consecutive_pebbles = 1
    next_tile_to_check = [x,y]
    curr_length = 1
    curr_start = [x, y]
    curr_end = [x, y]

    ## Up
    while next_tile_to_check[0]-1 >= 0: # = Lower border not reached
        next_tile_to_check[0] -= 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            curr_start[0] -= 1
            curr_length += 1
        else:
            break

    ## Down
    next_tile_to_check = [x, y]
    while next_tile_to_check[0]+1 < board.n():  # = Upper border not reached
        next_tile_to_check[0] += 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            curr_end[0] += 1
            curr_length += 1
        else:
            break

    if curr_length == n:
        result.append((curr_length, curr_start, curr_end))

    # Main diagonal check ==================================================================
    consecutive_pebbles = 1
    next_tile_to_check = [x,y]
    curr_length = 1
    curr_start = [x, y]
    curr_end = [x, y]

    ## Up & left
    while (next_tile_to_check[0]-1 >= 0) and (next_tile_to_check[1]-1 >= 0): # = Upper corner not reached
        next_tile_to_check[0] -= 1
        next_tile_to_check[1] -= 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            curr_start[0] -= 1
            curr_start[1] -= 1
            curr_length += 1
        else:
            break

    ## Down & right
    next_tile_to_check = [x, y]
    while (next_tile_to_check[0]+1 < board.n()) and (next_tile_to_check[1]+1 < board.n()):  # = Lower corner not reached
        next_tile_to_check[0] += 1
        next_tile_to_check[1] += 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            curr_end[0] += 1
            curr_end[1] += 1
            curr_length += 1
        else:
            break

    if curr_length == n:
        result.append((curr_length, curr_start, curr_end))

    # Secondary diagonal check ==================================================================
    consecutive_pebbles = 1
    next_tile_to_check = [x, y]
    curr_length = 1
    curr_start = [x, y]
    curr_end = [x, y]

    ## Up & right
    while (next_tile_to_check[0]-1 >= 0) and (next_tile_to_check[1]+1 < board.n()):  # = Upper corner not reached
        next_tile_to_check[0] -= 1
        next_tile_to_check[1] += 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            curr_end[0] -= 1
            curr_end[1] += 1
            curr_length += 1
        else:
            break

    ## Down & left
    next_tile_to_check = [x, y]
    while (next_tile_to_check[0]+1 < board.n()) and (next_tile_to_check[1]-1 >= 0):  # = Lower corner not reached
        next_tile_to_check[0] += 1
        next_tile_to_check[1] -= 1
        if board.get_pebble_type(next_tile_to_check[0], next_tile_to_check[1]) == pebble_type:
            consecutive_pebbles += 1
            curr_start[0] += 1
            curr_start[1] -= 1
            curr_length += 1
        else:
            break

    if curr_length == n:
        result.append((curr_length, curr_start, curr_end))

    return result

def calculate_orientation(start, end):
    """
    Calculates the orientation of a segment with endpoint 'start' and 'end'.
    :return: 1 = horizontal
             2 = vertical
             3 = main diagonal
             4 = secondary diagonal
    """
    if start[0] == end[0]:
        return 1
    if start[1] == end[1]:
        return 2
    if start[0] < end[0]:
        return 3
    if start[0] > end[0]:
        return 4

def check_open_ended_formation(board, formation):
    """
    :param formation: a tuple (m,[x1,y1],[x2,y2]).
    :return: True if the formation could become a 5-one, False if there is some pebble blocking.
    """
    if formation[0] == 5:
        return True

    orientation = calculate_orientation(formation[1], formation[2])
    orientation_expansions = [((),()), ((0,-1),(0,1)), ((-1,0),(1,0)), ((-1,-1),(1,1)), ((1, 1),(-1,1))]


    if formation[0] == 4:
        # start direction
        try:
            next_step_x = formation[1][0] + orientation_expansions[orientation][0][0]
            next_step_y = formation[1][1] + orientation_expansions[orientation][0][1]
            if board.get_pebble_type(next_step_x, next_step_y) == -1:
                return True
        except IndexError as ie:
            pass

        # end direction
        try:
            next_step_x = formation[2][0] + orientation_expansions[orientation][1][0]
            next_step_y = formation[2][1] + orientation_expansions[orientation][1][1]
            if board.get_pebble_type(next_step_x, next_step_y) == -1:
                return True
        except IndexError as ie:
            pass

    if formation[0] == 3:
        count = 0
        # start direction
        try:
            next_step_x = formation[1][0] + orientation_expansions[orientation][0][0]
            next_step_y = formation[1][1] + orientation_expansions[orientation][0][1]
            if board.get_pebble_type(next_step_x, next_step_y) == -1:
                count += 1
                try:
                    next_step_x = next_step_x + orientation_expansions[orientation][0][0]
                    next_step_y = next_step_y + orientation_expansions[orientation][0][1]
                    if board.get_pebble_type(next_step_x, next_step_y) == -1:
                        count += 1
                        return True
                except IndexError as ie:
                    pass
            else:
                return False
        except IndexError as ie:
            pass

        # end direction
        try:
            next_step_x = formation[2][0] + orientation_expansions[orientation][1][0]
            next_step_y = formation[2][1] + orientation_expansions[orientation][1][1]
            if board.get_pebble_type(next_step_x, next_step_y) == -1:
                count += 1
                try:
                    next_step_x = next_step_x + orientation_expansions[orientation][1][0]
                    next_step_y = next_step_y + orientation_expansions[orientation][1][1]
                    if board.get_pebble_type(next_step_x, next_step_y) == -1:
                        count += 1
                        return True
                except IndexError as ie:
                    pass
            else:
                return False
        except IndexError as ie:
            pass

        if count >= 2:
            return True

    return False

def check_formation_could_be_bigger(board, formation):
    """
    :param formation: a tuple (m,[x1,y1],[x2,y2]).
    :return: True if the formation could become a 5-one, False if there is some pebble blocking.
    """
    orientation = calculate_orientation(formation[1], formation[2])
    orientation_expansions = [((),()), ((0,-1),(0,1)), ((-1,0),(1,0)), ((-1,-1),(1,1)), ((1, 1),(-1,1))]
    pebble_type = board.get_pebble_type(formation[1][0], formation[1][1])

    check_1 = False
    check_2 = False
    # start direction
    try:
        next_step_x = formation[1][0] + orientation_expansions[orientation][0][0]
        next_step_y = formation[1][1] + orientation_expansions[orientation][0][1]
        if board.get_pebble_type(next_step_x, next_step_y) == -1:
            try:
                next_step_x = next_step_x + orientation_expansions[orientation][0][0]
                next_step_y = next_step_y + orientation_expansions[orientation][0][1]
                if board.get_pebble_type(next_step_x, next_step_y) == pebble_type:
                    check_1 = True
                    return True
            except IndexError as ie:
                pass
    except IndexError as ie:
        pass

    # end direction
    try:
        next_step_x = formation[2][0] + orientation_expansions[orientation][1][0]
        next_step_y = formation[2][1] + orientation_expansions[orientation][1][1]
        if board.get_pebble_type(next_step_x, next_step_y) == -1:
            try:
                next_step_x = next_step_x + orientation_expansions[orientation][1][0]
                next_step_y = next_step_y + orientation_expansions[orientation][1][1]
                if board.get_pebble_type(next_step_x, next_step_y) == pebble_type:
                    check_2 = True
                    return True
            except IndexError as ie:
                pass
    except IndexError as ie:
        pass

    if check_1 and check_2:
        return True
    return False



def find_first_pebble_of_given_type(board, type, start=[0,0]):
    """
    :param type: the pebble type
    :param start: Opt param, if specified the search will only start from those coords
    :return:
    """
    # if start != [0,0]:
    #     for i in range(board.n()):
    #         for j in range(board.n()):
    #             if board.get_pebble_type(i,j) == type:
    #                 return i,j
    # else:
    for j in range(start[1], board.n()):
        if board.get_pebble_type(start[0], j) == type:
            return int(start[0]), j
    for i in range(start[0]+1, board.n()):
        for j in range(board.n()):
            if board.get_pebble_type(i, j) == type:
                return i, j