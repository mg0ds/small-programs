rectangle = [[0, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 1, 1, 0]]

small = [[0, 0, 0],
         [0, 1, 0],
         [0, 0, 0]]

empty = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

whole = [[1, 1, 1],
         [1, 0, 1],
         [1, 1, 1]]

"""
Measure the size of an island in the ocean, based on the 2D map.
In this map, 0 represents ocean and 1 land.
There is only one island on the map.
The matrix cells are connected horizontally and vertically, not diagonally.
"""

def island_size(grid):
    try:
        rows = len(grid)
        columns = len(grid[0])
        total_nb = 0

        def check_nb(row, col):
            where_to_go = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            nb_count = 0
            for x, y in where_to_go:
                r = row + x
                c = col + y
                if r in range(rows) and c in range(columns) and grid[r][c] == 1:
                    nb_count += 1
            return nb_count

        def check_size(grid):
            #check maximum possible perimeter
            island_size = 0
            for r in grid:
                for c in r:
                    if c == 1:
                        island_size += 1
            return island_size

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    total_nb += check_nb(r, c)

        # each element can have perimeter = 4, when we knew how many elements there is, we just need to know
        # if adjacent tile is 1 or 0, if 1 then we need to subtract from max perimeter.
        perimeter = check_size(grid)*4 - total_nb
        return perimeter
    except:
        return 0
