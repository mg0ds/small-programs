from collections import deque

# Breadth First Search pathfinding algorithm

def check_neighbors(node):
    # take positions in all four directions that we can go to
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    can_go_to = []
    for dir in directions:
        neighbor = (node[0] + dir[0], node[1] + dir[1])
        if neighbor in grid: # check if position is in range
            can_go_to.append(neighbor)
    return can_go_to


"""
00000
01100
10000
10111
00000
"""
test_grid = [[(0, 0, True), (0, 1, True), (0, 2, True), (0, 3, True), (0, 4, True)],
[(1, 0, True), (1, 1, False), (1, 2, False), (1, 3, True), (1, 4, True)],
[(2, 0, False), (2, 1, True), (2, 2, True), (2, 3, True), (2, 4, True)],
[(3, 0, False), (3, 1, True), (3, 2, False), (3, 3, False), (3, 4, False)],
[(4, 0, True), (4, 1, True), (4, 2, True), (4, 3, True), (4, 4, True)]]

# remove nonpassable(walls) nodes
grid = set()
for line in test_grid:
    for poz in line:
        if poz[2]:
            grid.add((poz[0], poz[1]))

start = (0, 0)
end = (4, 4)

# list to place nodes that are at boundary of our expanding search algorithm
boundary = deque([start])
came_from = dict()
came_from[start] = None

while boundary:
    # remove first element from list
    current = boundary.popleft()
    # and check it's neighbors in all directions
    can_go_to = check_neighbors(current)
    for neighbor in can_go_to:
        # omit the ones that we already visited
        if neighbor not in came_from:
            # boundary enlarge
            boundary.append(neighbor)
            # save info from which position we came from
            came_from[neighbor] = current

# restore path from end to start
path_end_to_start = []
current_poz = end

while current_poz != start:
    path_end_to_start.append(current_poz)
    current_poz = came_from[current_poz]
path_end_to_start.append(start)
# our path is from end to start so it needs to be reversed
print(path_end_to_start[::-1])

