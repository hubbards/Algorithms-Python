'''
Script to test algorithm for sequence alignment problem.

NOTE: the worst-case time complexity of compute-opt (and find-solution) is
      O(m * n).
'''

def printf(m, n, x, y, memo, sol):
  '''
  TODO: comment
  '''
  left = []
  right = []
  for i in range(m + 1):
    left.append(0)
  for j in range(n + 1):
    right.append(0)
  for p in sol:
    left[p[0]] = p[1]
    right[p[1]] = p[0]
  sx = ''
  sy = ''
  i = 1
  j = 1
  for k in range(m + n - len(sol)):
    if left[i] == j:
      assert right[j] == i
      sx = sx + x[i]
      sy = sy + y[j]
      i = i + 1
      j = j + 1
    else:
      assert left[i] == 0 or right[j] == 0
      if left[i] == 0:
        sx = sx + x[i]
        sy = sy + '-'
        i = i + 1
      else:
        sx = sx + '-'
        sy = sy + y[j]
        j = j + 1
  print 'optimal solution: '
  print '               x: ' + sx
  print '               y: ' + sy
  print 'optimal value   : ' + str(memo[m][n])

def compute_opt(m, n, x, y, delta, epsilon):
  '''
  Function for algorithm that solves sequence alignment problem using dynamic
  programming method.

  '''
  memo = []
  row = []
  for j in range(n + 1):
    row.append(delta * j)
  memo.append(row)
  for i in range(1, m + 1):
    row = []
    row.append(delta * i)
    for j in range(1, n + 1):
      a = memo[i - 1][j] + delta
      b = row[j - 1] + delta
      c = memo[i - 1][j - 1] + epsilon[x[i] + y[j]]
      row.append(min(a, b, c))
      #if a >= c and b >= c:
      #  row.append(c)
      #elif a >= b:
      #  row.append(b)
      #else:
      #  row.append(a)
    memo.append(row)
  return memo

def find_sol(i, j, x, y, delta, memo, sol):
  '''
  Function to back-track through list of optimal values for sub-problems to
  find optimal solution.

  '''
  if i != 0 and j != 0:
    a = memo[i - 1][j] + delta
    b = memo[i][j - 1] + delta
    #c = memo[i - 1][j - 1] + epsilon[x[i] + y[j]]
    if memo[i][j] == a:
      find_sol(i - 1, j, x, y, delta, memo, sol)
    elif memo[i][j] == b:
      find_sol(i, j - 1, x, y, delta, memo, sol)
    else:
      sol.append((i, j))
      find_sol(i - 1, j - 1, x, y, delta, memo, sol)

# simple example if running as a program
if __name__ == '__main__':
  # simple example
  delta = 1
  epsilon = {'aa' : 0, 'ac' : 1, 'ae' : 3, 'an' : 1, 'ao' : 1, 'ar' : 1, \
             'au' : 1, \
             'ca' : 1, 'cc' : 0, 'ce' : 1, 'cn' : 1, 'co' : 1, 'cr' : 1, \
             'cu' : 1, \
             'ea' : 3, 'ec' : 1, 'ee' : 0, 'en' : 1, 'eo' : 1, 'er' : 1, \
             'eu' : 1, \
             'na' : 1, 'nc' : 1, 'ne' : 1, 'nn' : 0, 'no' : 1, 'nr' : 1, \
             'nu' : 1, \
             'oa' : 1, 'oc' : 1, 'oe' : 1, 'on' : 1, 'oo' : 0, 'or' : 1, \
             'ou' : 1, \
             'ra' : 1, 'rc' : 1, 're' : 1, 'rn' : 1, 'ro' : 1, 'rr' : 0, \
             'ru' : 1, \
             'ua' : 1, 'uc' : 1, 'ue' : 1, 'un' : 1, 'uo' : 1, 'ur' : 1, \
             'uu' : 0}
  x = ' ocurrance'
  y = ' occurrence'
  m = 9
  n = 10
  memo = compute_opt(m, n, x, y, delta, epsilon)
  sol = []
  find_sol(m, n, x, y, delta, memo, sol)
  printf(m, n, x, y, memo, sol)
  ## print 'optimal solution: ' + str(sol)
  ## print 'optimal value   : ' + str(memo[m][n])
