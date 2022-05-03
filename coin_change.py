#british = [1, 2, 5, 10, 20, 50]
#usa = [1, 5, 10, 25, 50]

def make_changes(n, coins):
    """
    Input: n - the changes amount
          coins - the coin denominations
    Output: how many ways to make this changes
    """
    combinations = [0 for i in range(n+1)]
    combinations[0] = 1
    for coin in coins:
        if n >= coin:
            for amount in range(1, n+1):
                if amount >= coin:
                    combinations[amount] += combinations[amount - coin]
    return combinations[-1]
