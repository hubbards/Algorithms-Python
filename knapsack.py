'''
Script to test algorithms for subset sum and knapsack problems.

NOTE: the worst-case time complexity of compute-opt (and find-solution) is
      O(n * W).
'''

def compute_opt1(m, n, w):
  '''
  Function for algorithm that solves subset sum problem using dynamic
  programming method.

  @param m: number of requests

  @param n: non-negative cut-off weight (or time)

  @param w: list of non-negative weights (or times) (numbers with positive
            indices)

  @return : list of optimal values for sub-problems
  '''
  memo = []
  # initialize memo
  for i in range(m + 1):
    row = []
    for j in range(n + 1):
      row.append(0)
    memo.append(row)
  # bottom-up computation of optimal values
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      a = memo[i - 1][j]
      if w[i] > j:
        memo[i][j] = a
      else:
        b = w[i] + memo[i - 1][j - w[i]]
        if a <= b:
          memo[i][j] = b
        else:
          memo[i][j] = a
  return memo

def compute_opt2(m, n, w, v):
  '''
  Function for algorithm that solves knapsack problem using dynamic
  programming method.

  @param m: number of requests

  @param n: non-negative cut-off weight (or time)

  @param w: list of non-negative weights (or times) (numbers with positive
            indices)

  @param v: list of values (numbers with positive indices)

  @return : list of optimal values for sub-problems
  '''
  memo = []
  # initialize memo
  for i in range(m + 1):
    row = []
    for j in range(n + 1):
      row.append(0)
    memo.append(row)
  # bottom-up computation of optimal values
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      a = memo[i - 1][j]
      if w[i] > j:
        memo[i][j] = a
      else:
        b = v[i] + memo[i - 1][j - w[i]]
        #memo[i][j] = max(a, b)
        if a <= b:
          memo[i][j] = b
        else:
          memo[i][j] = a
  return memo

def find_sol1(i, j, w, memo, sol):
  '''
  Function to back-track through list of optimal values for sub-problems to
  find optimal solution.

  @param i   : number of requests in sub-problem

  @param j   : non-negative cut-off weight (or time) in sub-problem

  @param w   : list of non-negative weights (or times) (numbers with positive
               indices)

  @param memo: list of optimal values for sub-problems

  @param sol : list of requests in optimal solution
  '''
  # top-down search for optimal solution
  if i > 0:
    if w[i] <= j:
      a = w[i] + memo[i - 1][j - w[i]]
      if memo[i][j] == a:
        sol.append(i)
        find_sol1(i - 1, j - w[i], w, memo, sol)
      else:
        find_sol1(i - 1, j, w, memo, sol)
    else:
      find_sol1(i - 1, j, w, memo, sol)

def find_sol2(i, j, w, v, memo, sol):
  '''
  Function to back-track through list of optimal values for sub-problems to
  find optimal solution.

  @param i   : number of requests in sub-problem

  @param j   : non-negative cut-off weight (or time) in sub-problem

  @param w   : list of non-negative weights (or times) (numbers with positive
               indices)

  @param v   : list of values (numbers with positive indices)

  @param memo: list of optimal values for sub-problems

  @param sol : list of requests in optimal solution
  '''
  # top-down search for optimal solution
  if i > 0:
    if w[i] <= j:
      a = v[i] + memo[i - 1][j - w[i]]
      if memo[i][j] == a:
        sol.append(i)
        find_sol2(i - 1, j - w[i], w, v, memo, sol)
      else:
        find_sol2(i - 1, j, w, v, memo, sol)
    else:
      find_sol2(i - 1, j, w, v, memo, sol)

# simple example if running as a program
if __name__ == '__main__':
  # simple example
  w = [0, 1, 2, 5, 6, 7]
  v = [0, 1, 6, 18, 22, 28]
  m = 5
  n = 11
  memo = compute_opt2(m, n, w, v)
  sol = []
  find_sol2(m, n, w, v, memo, sol)
  print 'optimal solution: ' + str(sol)
  print 'optimal value   : ' + str(memo[5][11])

