community = [3, 2, 6,  4, 7,  5, -8, -9, 3,  8,  4, -12, 3, -10, -15,
             2, 6, -10, 6, 3, -1,  5, -5, -8, 11, 7, -9, -5,  -6, -2,
             7, 8, 11, 8,  6, -1, -6,  9, 8, 6, -3, 4,  -8, 3, -4, 1,
             2, 8, -2, 9, -3, 8, -10,  -8,  5,  -4, -6,  5, -1, 4, 2,
             2, 7,  3, -2, 5, 1, 4, -7, 5, 8, 4, 2, 10, -24, -10, -9,
             -2, 1, 6, 1,  3, -44, 3, 6, -1, 9, -6, 5, 4, 3, 6, -1,
             0, 11, 4, 8, 16, -33, 8, -2, 4, 5, 3, 2, -8, -7, -5,
             0, 2, 5, -2, 4, 1, 2, 4, 2, -5, 7, 4, 5, -2, 7, 5, -8]

poverty = [0, -3, 2, 1, -7, 5, 3, -1, 6]
some = [2, -3, 2, 1, -7, -5, 3, -6, 18, 7, 13, 12]
extreme = [-1, -2, -3, -4, -5, -1, -2, -3]
test = [-2, 90, -1, -1, -1, -1, -1, 20]
test2 = [-2, 90, -1, -1, -1, -1, -1]

IMPOSSIBLE = 'Mission impossible. No one can contribute.'


def max_fund(village):
    """Find a contiguous subarray with the largest sum."""
    # Hint: while iterating, you could save the best_sum collected so far
    # return total, starting, ending
    i = 1
    sum = 0
    prev_sum = 0
    index_start = 0
    index_end = 0
    prev_index_end = 0
    for current in village:
        if sum > prev_sum:
            prev_sum = sum
            prev_index_end = i - 1
        if sum + current > 0:
            sum += current
            if index_start == 0:
                index_start = i
        else:
            sum = 0
            index_start = 0
        if i == len(village):
            if prev_sum > sum:
                sum = prev_sum
                index_end = prev_index_end
            else:
                index_end = i
        i += 1
        if sum == 0:
            index_end = 0
    return sum, index_start, index_end


print(max_fund(poverty))
