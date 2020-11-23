"""
This module contains a dynamic programming algorithm for solving the RNA
secondary structure problem. See section 6.5 of Algorithm Design by Kleinberg
and Tardos.

An instance of the RNA secondary structure problem is defined by a single-
stranded RNA molecule, i.e., a string of the characters (bases) A, C, G, and U.
A solution is a secondary structure, i.e., a set of non-crossing, matched base
pairs without any sharp turns. An optimal secondary structure is a secondary
structure with maximum number of matches.
"""

def base_pairs(x, y):
    """
    TODO document
    """
    return x == 'A' and y == 'U' or x == 'U' and y == 'A' or \
           x == 'C' and y == 'G' or x == 'G' and y == 'C'

def compute_opt(bs):
    """
    TODO document recurrence relation
    """
    # assert len(bs) > 5
    memo = [[0] * (i + 5) for i in range(len(bs) - 5)]
    for k in range(5, len(bs)):
        for i in range(len(bs) - k):
            j = i + k
            v1 = memo[i][j - 1]
            for t in range(i, j - 4):
                if base_pairs(bs[t], bs[j]):
                    v2 = 1 + (memo[i][t - 1] if t > i else 0) + memo[t + 1][j - 1]
                    v1 = max(v1, v2)
            memo[i].append(v1)
    return memo

def find_sol(bs, memo):
    """
    TODO document
    """
    # TODO implement
    return []

# Self-test
if __name__ == '__main__':
    bs = 'ACCGGUAGU' # bs = 'AUGUGGCCAU'

    memo = compute_opt(bs)
    ss = find_sol(bs, memo)

    print('single-stranded RNA molecule:' + bs)
    print('optimal secondary structure :' + ss)
