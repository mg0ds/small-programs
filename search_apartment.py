"""
Sample:

  A = [3, 5, 4, 4, 7, 1, 3, 2]  # central tallest
  B = [1, 1, 1, 1, 1, 2]  # almost flat
  C = [3, 5, 4, 3, 3, 1]
  #
  #  W <-                    ->  E(ast)
  #
  print(search_apartment(A, "W"))  # [0, 1, 4]
  print(search_apartment(A, "E"))  # [4, 6, 7]
  print(search_apartment(B, "W"))  # [0, 5]
  print(search_apartment(B, "E"))  # [5]
  print(search_apartment(C, "W"))  # [0, 1]
  print(search_apartment(C, "E"))  # [1, 2, 4, 5]
"""

def search_apartment(buildings: List[int], direction: str) -> List[int]:
    """
    Find and return the indices of those building with
    the desired view: EAST (E) or WEST (W).
    """
    prev_highest = 0
    output = []

    if direction == "W":
        i = 0
        for bldg in buildings:
            if i == 0:
                output.append(i)
                prev_highest = bldg
            elif bldg > prev_highest:
                output.append(i)
                prev_highest = bldg
            i += 1
        return output
    elif direction == "E":
        i = len(buildings) - 1
        for bldg in buildings[::-1]:
            if i == len(buildings) - 1:
                output.append(i)
                prev_highest = bldg
            elif bldg > prev_highest:
                output.append(i)
                prev_highest = bldg
            i -= 1
        return output[::-1]
