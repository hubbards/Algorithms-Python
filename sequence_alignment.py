"""
This module contains a dynamic programming algorithm for solving the sequence
alignment problem. See section 6.6 of Algorithm Design by Kleinberg and Tardos.

An instance of the sequence alignment problem is defined by a pair of strings,
a positive gap penalty, and mismatch costs for each pair of letters. A solution
is an alignment of the strings, i.e., a set of matched pairs of letters without
any crossing pairs. The cost of an alignment is the sum of mismatch costs for
matched letters and the product of the gap penalty and the number of unmatched
letters. An optimal alignment is an alignment with minimum cost.
"""

def compute_opt(d, a, xs, ys):
    """
    TODO document recurrence relation
    """
    # TODO initialize memo similar to knapsack.py and subset_sum.py
    memo = []
    for i, x in enumerate(xs):
        memo.append([])
        for j, y in enumerate(ys):
            c1 = a[x + y] + memo[i - 1][j - 1] if i > 0 and j > 0 else a[x + y]
            c2 = d + memo[i - 1][j] if i > 0 else (j + 1) * d
            c3 = d + memo[i][j - 1] if j > 0 else (i + 1) * d
            memo[i].append(min(c1, c2, c3))
    return memo

def find_sol(d, a, xs, ys, memo):
    """
    TODO document
    """
    sol = []
    i = len(xs) - 1
    j = len(ys) - 1
    while i >= 0 and j >= 0:
        c1 = a[xs[i] + ys[j]] + memo[i - 1][j - 1] if i > 0 and j > 0 else a[xs[i] + ys[j]]
        c2 = d + memo[i - 1][j] if i > 0 else (j + 1) * d
        c3 = d + memo[i][j - 1] if j > 0 else (i + 1) * d
        if memo[i][j] == c1:
            sol.append((i, j))
            i -= 1
            j -= 1
        elif memo[i][j] == c2:
            i -= 1
        else:
            assert memo[i][j] == c3
            j -= 1
    return sol

# Self-test
if __name__ == '__main__':
    # Gap character
    GAP = '-'

    # Pretty print alignment
    def pretty(d, a, xs, ys):
        # Find alignment
        memo = compute_opt(d, a, xs, ys)
        sol = find_sol(d, a, xs, ys, memo)
        sol.sort()
        # Build pretty alignment strings
        us = ''
        vs = ''
        i = 0
        j = 0
        for k, l in sol:
            # Add unaligned characters of xs
            us += xs[i:k]
            vs += GAP * (k - i)
            # Add unaligned characters of ys
            vs += ys[j:l]
            us += GAP * (l - j)
            # Add match
            us += xs[k]
            vs += ys[l]
            # Update indices
            i = k + 1
            j = l + 1
        # Add trailing unaligned characters of xs
        us += xs[i:]
        vs += GAP * (len(xs) - i)
        # Add trailing unaligned characters of ys
        vs += ys[j:]
        us += GAP * (len(ys) - j)
        # Print
        print('alignment: ')
        print('        x: ' + us)
        print('        y: ' + vs)
        print('     cost: ' + str(memo[-1][-1]))

    d = 1
    a = {'aa' : 0, 'ac' : 1, 'ae' : 3, 'an' : 1, 'ao' : 1, 'ar' : 1, 'au' : 1, \
         'ca' : 1, 'cc' : 0, 'ce' : 1, 'cn' : 1, 'co' : 1, 'cr' : 1, 'cu' : 1, \
         'ea' : 3, 'ec' : 1, 'ee' : 0, 'en' : 1, 'eo' : 1, 'er' : 1, 'eu' : 1, \
         'na' : 1, 'nc' : 1, 'ne' : 1, 'nn' : 0, 'no' : 1, 'nr' : 1, 'nu' : 1, \
         'oa' : 1, 'oc' : 1, 'oe' : 1, 'on' : 1, 'oo' : 0, 'or' : 1, 'ou' : 1, \
         'ra' : 1, 'rc' : 1, 're' : 1, 'rn' : 1, 'ro' : 1, 'rr' : 0, 'ru' : 1, \
         'ua' : 1, 'uc' : 1, 'ue' : 1, 'un' : 1, 'uo' : 1, 'ur' : 1, 'uu' : 0}
    xs = 'ocurrance'
    ys = 'occurrence'

    pretty(d, a, xs, ys)
