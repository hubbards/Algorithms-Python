'''
Script to test algorithm for RNA secondary structure problem.

NOTE: the worst-case time complexity of compute-opt (and find-solution) is
      O(n ** 3).
'''

def find_max(i, j, s, memo):
  '''
  Function to find optimal value and solution (to sub-problem) if last index
  is paired with some index between first and last index.

  @param i   : first index

  @param j   : last index

  @param s   : string for RNA sequence (characters with positive indices)

  @param memo: list of optimal values for sub-problems

  @return    : optimal value and solution if last index is paired with some
               index between first and last index
  '''
  a1 = -1
  k1 = -1
  k2 = i
  while k2 < j - 4:
    # k2 and j satisfy "no sharp turn" condition
    if (s[k2] == 'A' and s[j] == 'U') or (s[k2] == 'U' and s[j] == 'A') or \
       (s[k2] == 'C' and s[j] == 'G') or (s[k2] == 'G' and s[j] == 'C'):
      # k2 and j satisfy "base pair" condition
      a2 = 1 + memo[i][k2 - 1] + memo[k2 + 1][j - 1]
      if a1 < a2:
        a1 = a2
        k1 = k2
    k2 = k2 + 1
  return (k1, a1)

def compute_opt(n, s):
  '''
  Function for algorithm that solves RNA secondary structure problem using
  dynamic programming method.

  @param n: length of RNA sequence

  @param s: string for RNA sequence (characters with positive indices)

  @return : list of optimal values for sub-problems
  '''
  memo = []
  # initialize memo
  for i in range(n + 1):
    row = []
    for j in range(n + 1):
      row.append(0)
    memo.append(row)
  # bottom-up computation of optimal values, i.e., shortest intervals first
  for k in range(5, n):
    for i in range(1, n - k + 1):
      # interval of length k + 1
      j = i + k
      a = memo[i][j - 1]
      p = find_max(i, j, s, memo)
      #memo[i][j] = max(a, p[1])
      if a <= p[1]:
        memo[i][j] = p[1]
      else:
        memo[i][j] = a
  return memo

def find_sol(i, j, s, memo, sol):
  '''
  Function to back-track through list of optimal values for sub-problems to
  find optimal solution.

  @param i   : first index

  @param j   : last index

  @param s   : string for RNA sequence (characters with positive indices)

  @param memo: list of optimal values for sub-problems

  @param sol : list of pairs in optimal solution
  '''
  # top-down search for optimal solution
  if i < j - 4:
    p = find_max(i, j, s, memo)
    if memo[i][j] == p[1]:
      sol.append((p[0], j))
      find_sol(p[0] + 1, j - 1, s, memo, sol)
      find_sol(i, p[0] - 1, s, memo, sol)
    else:
      find_sol(i, j - 1, s, memo, sol)

# simple example if running as a program
if __name__ == '__main__':
  # simple example
  s = ' AUGUGGCCAU'
  n = 10
  memo = compute_opt(n, s)
  sol = []
  find_sol(1, n, s, memo, sol)
  print 'optimal solution: ' + str(sol)
  print 'optimal value   : ' + str(memo[1][10])

