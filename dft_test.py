'''
Script to test discrete Fourier transform (DFT) algorithms.

TODO: document algorithms

TODO: document running times

TODO: inverse transform algorithms
'''

import cmath

def dft(n, x):
  '''
  Function for discrete Fourier transform algorithm using direct method, i.e.,
  matrix multiplying coefficient vector by Fourier matrix.

  @param n: degree of polynomial + 1

  @param x: vector of complex coefficients of polynomial, i.e., coefficient
            representation of polynomial

  @return : vector of values of polynomial evaluated at n^th roots of unity,
            i.e., point-value representation of polynomial
  '''
  y = []
  zeta = cmath.exp(2 * cmath.pi * 1j / n) # principle n^th root of unity
  for i in range(n):
    tmp1 = zeta ** (i + 1)
    tmp2 = 0
    for j in range(n):
      tmp2 += tmp1 ** j * x[j]
    y.append(tmp2)
  return y

def fft(n, x):
  '''
  Function for discrete fast Fourier transform (FFT) algorithm using divide and
  conquer method, recursively computing FFT of even and odd order terms and
  merging results.

  @param n: degree of polynomial + 1

  @param x: vector of complex coefficients of polynomial, i.e., coefficient
            representation of polynomial

  @return : vector of values of polynomial evaluated at n^th roots of unity,
            i.e., point-value representation of polynomial

  @pre    : n is a power of 2
  '''
  if n == 1:
    return x
  e = [] # even order terms
  o = [] # odd order terms
  for i in range(n):
    if i % 2 == 0:
      e.append(x[i])
    else:
      o.append(x[i])
  m = n // 2
  e = fft(m, e) # FFT of even order terms
  o = fft(m, o) # FFT of odd order terms
  # merge results
  y = []
  for i in range(n):
    y.append(0)
  zeta = cmath.exp(2 * cmath.pi * 1j / n) # principle n^th root of unity
  for i in range(m):
    tmp = zeta ** (i + 1) * o[i]
    y[i] = e[i] + tmp
    y[i + m] = e[i] - tmp
  return y

def printf(x):
  '''
  Function that prints the given list of complex numbers as ordered pairs.
  '''
  n = len(x)
  a = x[0].real
  b = x[0].imag
  s = '[(%.2g,%.2g)' % (a, b)
  for i in range(1, n):
    a = x[i].real
    b = x[i].imag
    s += ', (%.2g,%.2g)' % (a, b)
  s += "]"
  print s

# simple example if running as a program
if __name__ == '__main__':
  # simple example
  x = [1, 1, 1, 1] # product of 2^nd and 4^th cyclotomic polynomials
  n = 4
  print "test dft"
  y = dft(n, x)
  printf(y)
  print "test fft"
  y = fft(n, x)
  printf(y)
