#!/usr/bin/env python3
from __future__ import print_function
from __future__ import with_statement
__author__ = 'sun.haixuan'


# Find PI to the Nth Digit
# Have the user enter a number 'n'
# and print out PI to the 'n'th digit


import decimal
def legendre(): #Gauss-Legendre Algorithm
    D = decimal.Decimal
    with decimal.localcontext() as ctx:
        ctx.prec += 2
        a, b, t, p = 1, 1/D(2).sqrt(), 1/D(4), 1
        pi = None
        while 1:
            an    = (a + b) / 2
            b     = (a * b).sqrt()
            t    -= p * (a - an) * (a - an)
            a, p  = an, 2*p
            piold = pi
            pi    = (a + b) * (a + b) / (4 * t)
            if pi == piold:
                break
    return +pi


def calcPi(limit):  # Generator function
    """
    Prints out the digits of PI
    until it reaches the given limit
    """

    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3

    decimal = limit
    counter = 0

    while counter != decimal + 1:
            if 4 * q + r - t < n * t:
                    # yield digit
                    yield n
                    # insert period after first digit
                    if counter == 0:
                            yield '.'
                    # end
                    if decimal == counter:
                            print('')
                            break
                    counter += 1
                    nr = 10 * (r - n * t)
                    n = ((10 * (3 * q + r)) // t) - 10 * n
                    q *= 10
                    r = nr
            else:
                    nr = (2 * q + r) * l
                    nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
                    q *= k
                    t *= l
                    l += 2
                    k += 1
                    n = nn
                    r = nr


def main():  # Wrapper function
    n = int(input("Enter the number of decimals to calculate to:"))
    if n <= 10000:
        digits = calcPi(n)
    else:
        print("The number of decimals exceeds the limit of 10000")

    for d in digits:
        print(d, end='')

if __name__ == '__main__':
    main()