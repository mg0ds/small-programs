"""
Input: 2D matrix
Output: number of islands, or 0 if found none.
Islands are represented by 1s, oceans by 0. If the 1s are connected either horizontally or vertically (not diagonally), then they count as one island. Count of number of islands as efficient as possible. If no islands are found, just return 0.
The goal is to find how many islands there are in the ocean, regardless of its size.
"""

squares = [[1, 1, 0, 1],
           [1, 1, 0, 1],
           [0, 0, 1, 1],
           [1, 1, 1, 0]]

sparse = [[1, 0, 1],
          [0, 1, 0],
          [1, 0, 1]]

empty = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

bad_map = [[]]

cos = []
cos2 = 2
cos3 = "asdasd"

circles = [[1, 1, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 1, 1],
           [1, 0, 0, 0, 1, 0],
           [1, 0, 0, 1, 1, 0],
           [1, 1, 1, 1, 0, 0]]

def count_islands(grid):
    try:
        rows = len(grid)
        columns = len(grid[0])
        island_num = 0
        visited = set()

        def check_nb(r, c):
            to_check = []
            to_check.append([r, c])
            visited.add((r, c))
            where_to_go = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while to_check:
                row, col = to_check[0]
                del to_check[0]
                for x, y in where_to_go:
                    r = row + x
                    c = col + y
                    if r in range(rows) and c in range(columns) and grid[r][c] == 1 and (r,c) not in visited:
                        to_check.append([r, c])
                        visited.add((r, c))

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1 and (r, c) not in visited:
                    check_nb(r, c)
                    island_num += 1
        #print(island_num)
        return island_num
    except:
        return 0
        
#run function to check islands
count_islands(squares)
