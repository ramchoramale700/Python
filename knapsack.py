
def knapsack(values, weights, capacity):
    n = len(values)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]

# Example data
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print(f"Maximum value in knapsack:", knapsack(values, weights,capacity))