def coinChange(coins, amount):
    """
    This solution works for coins which are multiples of smaller coins (or maybe just cases
    where a penny is in the register. My approach was to use as many of the largest coins
    as possible to reach the amount. When no more largest coins can be used, move on to
    the next largest coin and so forth.

    At least one test case of the coinChange problem uses coins with values that are
    not multiples of each other and was not solved by my approach.
    """
    register = {}
    coins.sort(reverse=True) # Check largest coins first
    # Initialize with count = 0 for each coin
    for coin in coins:
        register[coin] = 0

    for coin in register:
        while coin <= amount:
            register[coin] += 1 # Increment number of coins
            amount -= int(coin) # Remove value of coin from amount

    if amount > 0: return -1 # If there is still money left over, change couldn't be made
    return sum(register.values())

# print(coinChange([1], 0) == 0)
# print(coinChange([1], 2) == 2)
# print(coinChange([1,2,5], 11) == 3)
# print(coinChange([186,419,83,408], 6249))

def coinChange2(coins, amount):
    """
    This successful solution by jhacker uses Dynamic Programming which I am unfamiliar
    with. Following is my explaination of the algorithim.

    It starts by creating an array of elements (amount+1) amount+1 times and replacing the
    first index with 0. For example, if amount = 3, array = [0,4,4,4]. Change the first index
    to 0 is important

    Loop through the array and coin values, if a coin value is less than amount and the value
    of the array at minCoins[i-coin] is less than the current value of minCoins replace it with
    minCoins[i-coin] + 1.
    The first values to be changed will be at minCoin[n] where n is the value of a coin. Therefore,
    subsequent multiples of n and combinations of n with other n's will have their values changed.
    Finally, if the amount is able to be divided into coins it too will be changed and returned.
    If not, it will be unchanged and -1 will be returned.

    I kinda see how it works but am still a little lost by it
    """
    # Values in this array equal the number of coins needed to achieve the cost of the index
    minCoins = [amount + 1] * (amount + 1) # Add 1 to array bc [0] = 0, not sure about adding 1 to the value
    minCoins[0] = 0
    print(minCoins)

    for i in range(amount + 1):
        for coin in coins:
            # Check that the coin is lass than the current amount
            if coin <= i:
                # minCoins[i]: number of coins needed to make amount i
                # minCoins[i-coin]: number of coins needed to make the amount before adding
                #                   the current coin to it (+1 to add the current coin)
                minCoins[i] = min(minCoins[i], minCoins[i - coin] + 1) # Can't return index out of range bc coin > i
    print(minCoins)
    # If minCoins[-1] is unchanged it's not possible
    if minCoins[amount] == amount + 1:
        return -1
    # Return the optimal number of coins to create the amount
    return minCoins[amount]
# print(coinChange2([4,5], 11))
# print(coinChange2([2,5], 11))