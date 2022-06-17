import numpy as np

DOWN, UP, LEFT, RIGHT = '⇓', '⇑', '⇐', '⇒'
START_VALUE = 1

small_grid = """
21 - 22 - 23 - 24 - 25
 |
20    7 -  8 -  9 - 10
 |    |              |
19    6    1 -  2   11
 |    |         |    |
18    5 -  4 -  3   12
 |                   |
17 - 16 - 15 - 14 - 13
"""

intermediate_grid = """
43 - 44 - 45 - 46 - 47 - 48 - 49
 |
42   21 - 22 - 23 - 24 - 25 - 26
 |    |                        |
41   20    7 -  8 -  9 - 10   27
 |    |    |              |    |
40   19    6    1 -  2   11   28
 |    |    |         |    |    |
39   18    5 -  4 -  3   12   29
 |    |                   |    |
38   17 - 16 - 15 - 14 - 13   30
 |                             |
37 - 36 - 35 - 34 - 33 - 32 - 31
"""

intermediate2_grid = """
31 - 32 - 33 - 34 - 35 - 36 - 37
 |                             |
30   13 - 14 - 15 - 16 - 17   38
 |    |                   |    |
29   12    3 -  4 -  5   18   39
 |    |    |         |    |    |
28   11    2 -  1    6   19   40
 |    |              |    |    |
27   10 -  9 -  8 -  7   20   41
 |                        |    |
26 - 25 - 24 - 23 - 22 - 21   42
                               |
49 - 48 - 47 - 46 - 45 - 44 - 43
"""

def print_sequence_route(grid, start_coordinates=None):
    """Receive grid string, convert to 2D matrix of ints, find the
       START_VALUE coordinates and move through the numbers in order printing
       them.  Each time you turn append the grid with its corresponding symbol
       (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""
    visited = []
    visited_number = [1]
    direction_list = ["start"]
    
    def neighbour_check(grid, start_i, start_j, direction = None):
        visited.append([start_i, start_j])
        available_moves = []
        available_moves_poz = []
        moves = ((0, 1, RIGHT), (1, 0, DOWN), (-1, 0, UP), (0, -1, LEFT))
        for x, y, direction in moves:
            if [int(start_i) + x, int(start_j) + y] not in visited and \
                    ((int(start_i) + x) < len(grid) and (int(start_j) + y) < len(grid)) and \
                    ((int(start_i) + x) > -1 and (int(start_j) + y) > -1):
                available_moves.append([grid[int(start_i) + x][int(start_j) + y], direction])
                available_moves_poz.append([int(start_i) + x, int(start_j) + y, direction])
        if available_moves == []:
            return None
        else:
            next_step = available_moves_poz[available_moves.index(min(available_moves))]
            direction_list.append(next_step[2])
            if len(direction_list) > 2 and str(direction_list[-2]) != str(next_step[2]):
                visited_number.append(next_step[2])
                visited_number.append("\n")
                visited_number.append(grid[next_step[0]][next_step[1]])
            else:
                visited_number.append(grid[next_step[0]][next_step[1]])
            neighbour_check(grid, next_step[0], next_step[1], next_step[2])


    new_grid = grid.split("\n")
    clean_grid = []
    a = 0
    for i in new_grid:
        clean_grid.append([])
        for j in i.split():
            try:
                clean_grid[a].append(int(j))
            except:
                continue
        a += 1
    clean_grid = [element for element in clean_grid if element != []]
    
    # 1 location in grid:
    np_clean_grid = np.array(clean_grid)
    i, j = np.where(np_clean_grid == 1)
    neighbour_check(clean_grid, i[0], j[0])
    
    print(*visited_number)
