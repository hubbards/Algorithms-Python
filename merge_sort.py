"""
This module contains an implementation of the merge-sort algorithm.
"""

def sort(xs):
    """
    Sorts a given sequence of numbers.
    """
    if len(xs) > 1:
        m = len(xs) // 2
        ys = sort(xs[:m])
        zs = sort(xs[m:])
        xs = merge(ys, zs)
    return xs

def merge(xs, ys):
    """
    Merges two sorted sequences of numbers into one sorted sequence.
    """
    zs = []
    i = 0
    j = 0
    for k in range(len(xs) + len(ys)):
        if j >= len(ys) or i < len(xs) and xs[i] <= ys[j]:
            zs.append(xs[i])
            i += 1
        else:
            zs.append(ys[j])
            j += 1
    return zs

# Self-test
if __name__ == '__main__':
    xs = [2, 4, 1, 3, 5]
    ys = xs[:-1]
    print(sort(xs))
    print(sort(ys))
