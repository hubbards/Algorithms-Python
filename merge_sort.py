'''
Script to test merge-sort algorithm.

NOTE: The worst-case time complexity of the merge-sort algorithm is O(n*log(n)).
'''

def merge_sort1(a, p, q):
  '''
  Function to sort given sub-array.

  @param a: array of integers

  @param p: first index

  @param q: last index

  @pre    : 0 <= p <= q < len(a)
  '''
  m = q - p + 1
  if 1 < m:
    # recursive case
    r = m / 2 + p
    # sort left half
    merge_sort1(a, p, r - 1)
    # sort right half
    merge_sort1(a, r, q)
    # merge result
    merge1(a, p, r, q)

def merge1(a, p, r, q):
  '''
  Function to merge sorted halves.

  @param a: array of integers

  @param p: first index

  @param r: middle index

  @param q: last index

  @pre    : 0 <= p < r <= q < len(a)
  '''
  m = q - p + 1
  i = p
  j = r
  b = []
  for k in range(m):
    if q < j or i < r and a[i] <= a[j]:
      # take from left half
      b.append(a[i])
      i = i + 1
    else:
      # take from right half
      b.append(a[j])
      j = j + 1
  for k in range(m):
    a[p + k] = b[k]

def merge_sort2(a, b, p, q):
  '''
  Function to sort given sub-array.

  @param a: array of integers

  @param b: temporary array

  @param p: first index

  @param q: last index

  @pre    : 0 <= p <= q < len(a) == len(b)
  '''
  m = q - p + 1
  if 1 < m:
    # recursive case
    r = m / 2 + p
    # sort left half
    merge_sort2(a, b, p, r - 1)
    # sort right half
    merge_sort2(a, b, r, q)
    # merge result
    merge2(a, b, p, r, q)

def merge2(a, b, p, r, q):
  '''
  Function to merge sorted halves.

  @param a: array of integers

  @param b: temporary array

  @param p: first index

  @param r: middle index

  @param q: last index

  @pre    : 0 <= p < r <= q < len(a) == len(b)
  '''
  i = p
  j = r
  for k in range(p, q + 1):
    if q < j or i < r and a[i] <= a[j]:
      # take from left half
      b[k] = a[i]
      i = i + 1
    else:
      # take from right half
      b[k] = a[j]
      j = j + 1
  for k in range(p, q + 1):
    a[k] = b[k]

# simple example if running as program
if __name__ == '__main__':
  # simple example
  a1 = [2, 4, 1, 3, 5] # 3 inversions
  merge_sort1(a1, 0, 4)
  print a1
  a2 = [2, 4, 1, 3, 5] # 3 inversions
  b2 = [0, 0, 0, 0, 0]
  merge_sort2(a2, b2, 0, 4)
  print a2
