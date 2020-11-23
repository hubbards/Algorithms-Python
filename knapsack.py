"""
This module contains a dynamic programming algorithm for solving the knapsack
problem, which is a generalization of the subset sum problem. See section 6.4 of
Algorithm Design by Kleinberg and Tardos.

An instance of the knapsack problem is defined by a weight capacity and a
collection items, where each item has both a weight and value. A solution is any
subset of items for which the total weight does not exceed the capacity. An
optimal solution is a solution with maximum total value.
"""

def compute_opt(c, ws, vs):
    """
    Computes maximum total value for subproblems of the instance of the
    knapsack problem with weight capacity c, item weights ws, and item values
    vs.

    TODO document recurrence relation
    """
    memo = [[0] * (c + 1)] * len(ws)
    for i in range(len(ws)):
        for j in range(1, c + 1):
            v1 = memo[i - 1][j] if i > 0 else 0
            if j < ws[i]:
                memo[i][j] = v1
            else:
                v2 = vs[i] + (memo[i - 1][j - ws[i]] if i > 0 else 0)
                memo[i][j] = max(v1, v2)
    return memo

def find_sol(c, ws, vs, memo):
    """
    Finds an optimal solution for the given instance of the knapsack problem
    with weight capacity c, item weights ws, and item values vs, provided
    maximum total value for subproblems are memoized in memo.
    """
    sol = []
    for n in reversed(range(len(ws))):
        if c >= ws[n] and memo[n][c] == vs[n] + memo[n - 1][c - ws[n]]:
            sol.append(n)
            c -= ws[n]
    return sol

# Self-test
if __name__ == '__main__':
    # Pretty print optimal value and solution
    def pretty(c, ws, vs):
        memo = compute_opt(c, ws, vs)
        sol  = find_sol(c, ws, vs, memo)
        print('optimal value   : ' + str(memo[-1][c]))
        print('optimal solution: ' + str(sol))

    c = 11
    ws = [1, 2,  5,  6,  7]
    vs = [1, 6, 18, 22, 28]

    pretty(c, ws, vs)
