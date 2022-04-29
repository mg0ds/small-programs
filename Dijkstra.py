
import math

simple = {
          'a': {'b': 2, 'c': 4, 'e': 1},
          'b': {'a': 2, 'd': 3},
          'c': {'a': 4, 'd': 6},
          'd': {'c': 6, 'b': 3, 'e': 2},
          'e': {'a': 1, 'd': 2}
          }

major = {
          'a': {'w': 14, 'x': 7, 'y': 9},
          'b': {'w': 9, 'z': 6},
          'w': {'a': 14, 'b': 9, 'y': 2},
          'x': {'a': 7,  'y': 10, 'z': 15},
          'y': {'a': 9,  'w': 2, 'x': 10, 'z': 11},
          'z': {'b': 6,  'x': 15, 'y': 11},
        }


def shortest_path(graph, start, end):
    """
       Input: graph: a dictionary of dictionary
              start: starting city   Ex. a
              end:   target city     Ex. b

       Output: tuple of (distance, [path of cites])
       Ex.   (distance, ['a', 'c', 'd', 'b])
    """

    Q = list(graph.keys())
    S = []
    d = {x:math.inf for x in Q}
    d[start] = 0
    p = {x:-1 for x in Q}
    current = ""

    while Q != []:
        if S == []:
            S.append(start)
            Q.pop(Q.index(start))
            current = start
        else:
            min_d = math.inf
            for key, value in d.items():
                if key != start and value < min_d and key not in S:
                    min_d = value
                    current = key
            S.append(current)
            Q.pop(Q.index(current))

        for key, value in graph[current].items():
            if d[key] > d[current] + value:
                d[key] = d[current] + value
                p[key] = current
    
    #get path from start to end as list
    path_list = [end]
    def path(p, end):
        if p[end] == -1:
            return path_list
        else:
            path_list.append(p[end])
            path(p, p[end])
    path(p, end)
    
    return d[end], path_list[::-1]
