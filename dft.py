"""
The module contains algorithms for the discrete Fourier transform (DFT).

The DFT maps the coefficients of a degree n polynomial with complex coefficients
to value at the (n + 1)-th roots of unity, i.e., the point-value representation
of the polynomial.
"""

import cmath

def proot(n):
    """
    Returns the principle n-th root of unity.
    """
    assert n > 0
    return cmath.exp(2 * cmath.pi * 1j / n)

def dft(xs):
    """
    Computes the DFT of polynomial with coefficient vector xs using the direct
    method, i.e., matrix multiplication of coefficient vector by Fourier matrix.
    """
    ys = []
    zp = proot(len(xs))
    for i in range(len(xs)):
        z = zp ** (i + 1)
        y = 0
        for j in range(len(xs)):
            y += z ** j * xs[j]
        ys.append(y)
    return ys

def fft(xs):
    """
    Computes the DFT of polynomial with coefficient vector xs using the discrete
    fast Fourier transform (FFT) algorithm. A precondition of this function is
    len(xs) is a power of 2.
    """
    if len(xs) > 1:
        # Divide into even and odd order terms
        es = []
        os = []
        for i, x in enumerate(xs):
            if i % 2 == 0:
                es.append(x)
            else:
                os.append(x)
        m = len(xs) // 2
        es = fft(es)
        os = fft(os)
        # Merge results
        zp = proot(len(xs))
        for i in range(m):
            z = zp ** (i + 1) * os[i]
            xs[i] = es[i] + z
            xs[i + m] = es[i] - z
    return xs

# Self-test
if __name__ == '__main__':
    # Pretty print
    def pretty(cs):
        def helper(c): return '%.2g%+.2gi' % (c.real, c.imag)
        return str(list(map(helper, cs)))


    # Product of 2nd and 4th cyclotomic polynomials
    xs = [1, 1, 1, 1]

    print('DFT: ' + pretty(dft(xs)))
    print('FFT: ' + pretty(fft(xs)))
