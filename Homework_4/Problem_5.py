# Problem 5: Change-Making Problem
# Write Python code that solves the change-making problem.
# The change-making problem addresses the question of finding the minimum number of coins (of certain denominations) that add up to a given amount of money

# Step 1:  sort array of coins in decreasing order
def sort_coins(coins: list(int)) -> None:
    """
    Inplace sort coins in decreasing order
    :param coins: list of coins
    :return: None
    """
    for i in range(len(coins)):
        for j in range(i + 1, len(coins)):
            if coins[i] < coins[j]:
                coins[i], coins[j] = coins[j], coins[i]


# Step 2:  iterate over the coins to populate solution array
def change_making(coins: list(int), amount: int) -> list(int):
    """
    Find the minimum number of coins that add up to a given amount of money
    :param coins: Denominations of coins
    :param amount: Amount of money
    :return: list of coins
    """
    # sort coins in decreasing order
    sort_coins(coins)
    # empty solution array
    solution = []
    # iterate over the coins
    for coin in coins:
        # find the largest coin that is less than or equal to the amount
        while coin <= amount:
            # add the coin to the solution
            solution.append(coin)
            # subtract the coin from the amount
            amount -= coin
    return solution


if __name__ == "__main__":
    # Input:
    denominations = [1, 10, 100, 1000, 2, 20, 5, 50, 500]  # Dominations
    n = 1985  # Given amount in cents
    # Output:
    print(change_making(denominations, n))
