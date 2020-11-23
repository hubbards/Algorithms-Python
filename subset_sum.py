"""
This module contains a dynamic programming algorithm for solving the subset sum
problem. See section 6.4 of Algorithm Design by Kleinberg and Tardos.

An instance of the subset sum problem is defined by a weight capacity and a
collection of items, where each item has a weight. A solution is any subset of
items for which the total weight does not exceed the capacity. An optimal
solution is a solution with maximum total weight.
"""

def compute_opt(c, ws):
    """
    Computes the maximum total weight for subproblems of the given instance of
    the subset sum problem with weight capacity c and item weights ws.

    TODO document recurrence relation
    """
    memo = [[0] * (c + 1)] * len(ws)
    for i in range(len(ws)):
        for j in range(1, c + 1):
            w1 = ws[i] if i > 0 else 0
            if j < ws[i]:
                memo[i][j] = w1
            else:
                w2 = ws[i] + memo[i - 1][j - ws[i]] if i > 0 else ws[i]
                memo[i][j] = max(w1, w2)
    return memo

def find_sol(c, ws, memo):
    """
    Finds an optimal solution for the given instance of the subset sum problem
    with weight capacity c and item weights ws, provided maximum total weights
    for subproblems are memoized in memo.
    """
    sol = []
    for n in reversed(range(len(ws))):
        if c >= ws[n] and memo[n][c] == ws[n] + memo[n - 1][c - ws[n]]:
            sol.append(n)
            c -= ws[n]
    return sol

# Self-test
if __name__ == '__main__':
    # Pretty print optimal value and solution
    def pretty(c, ws):
        memo = compute_opt(c, ws)
        sol  = find_sol(c, ws, memo)
        print('optimal value   : ' + str(memo[-1][c]))
        print('optimal solution: ' + str(sol))

    c  = 11
    ws = [1, 2, 5, 6, 7]

    pretty(c, ws)
