# // Input:
# // Values (stored in array v)
# // Weights (stored in array w)
# // Number of distinct items (n)
# // Knapsack capacity (W)
# // NOTE: The array "v" and array "w" are assumed to store all relevant values starting at index 1.
# knapsack problem is only allowed to take each item ONCE thats why its 0/1

# array m[0..n, 0..W];
# for j from 0 to W do:
#     m[0, j] := 0
# for i from 1 to n do:
#     m[i, 0] := 0

# for i from 1 to n do:
#     for j from 1 to W do:
#         if w[i] > j then:
#             m[i, j] := m[i-1, j]
#         else:
#             m[i, j] := max(m[i-1, j], m[i-1, j-w[i]] + v[i])

import logging

logging.basicConfig(level=logging.WARNING)
# logging.basicConfig(level=logging.INFO)

def knapsack(v, w, n, W):
    # Create DP table (n+1 rows, W+1 cols) initialized to 0
    m = [[0] * (W + 1) for _ in range(n + 1)]

    # Base cases are already 0 (m[0][j] and m[i][0])

    # Fill the table
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if w[i] > j:
                # Can't take item i (too heavy)
                logging.info(f"{w[i]=}, {j=}, too much")
                m[i][j] = m[i - 1][j]
            else:
                # Either skip or take the item
                old = m[i-1][j]
                m[i][j] = max(
                    m[i - 1][j],                # Skip item
                    m[i - 1][j - w[i]] + v[i]   # Take item
                )
                logging.info(f"{w[i]=}, {j=}, take/skip, {old=}, {m[i][j]=}, j-w[i]={j - w[i]}")
        logging.info(f"{i=}, {m[i]=}")  # logging current row of DP table
    return m[n][W], m  # Return max value and full DP table


# Example usage:
# 1-indexed arrays for values and weights (index 0 is dummy)
values  = [0, 60, 100, 120]  # v[1]=60, v[2]=100, v[3]=120
weights = [0, 1, 20, 30]    # w[1]=10, w[2]=20, w[3]=30
n = 3
W = 30

max_value, dp_table = knapsack(values, weights, n, W)
logging.warning(f"Maximum value in knapsack: {max_value}")

# Optional: logging DP table
# logging("DP Table:")
# for row in dp_table:
#     logging(row)
