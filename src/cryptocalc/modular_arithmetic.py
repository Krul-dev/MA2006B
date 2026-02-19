# -*- coding: utf-8 -*-
"""
modular_arithmetic.py

Created on Fri Apr  6 14:59:45 2018

@author: raul
"""

from cryptocalc.euclid_algorithm import fast_extended_gcd


def simplify_mod(a, n):
    return (a % n, n)


def add_mod(x, y):
    return simplify_mod(x[0]+y[0], x[1])


def substract_mod(x, y):
    return simplify_mod(x[0]-y[0], x[1])


def multiply_mod(x, y):
    return simplify_mod(x[0]*y[0], x[1])


def divide_mod(x, y):
    return simplify_mod(x[0]*(fast_extended_gcd(y[1], y[0])[1]), x[1])


def naive_exp_mod(x, m):
    result = 1
    for i in range(m):
        result = (result * x[0]) % x[1]
    return (result, x[1])


def exp_mod(x, m):
    if m == 0:
        return (1, x[1])
    elif m == 1:
        return x
    elif m % 2 == 0:
        return exp_mod(multiply_mod(x, x), m // 2)
    else:
        return multiply_mod(x, exp_mod(multiply_mod(x, x), (m - 1) // 2))


def chinese_remainder(x, y):
    a = x[0]
    p = x[1]
    b = y[0]
    q = y[1]
    r = fast_extended_gcd(p, q)[0]
    s = fast_extended_gcd(p, q)[1]
    n = p*q
    z = b*p*r + a*q*s
    return simplify_mod(z, n)



def jacobi_symbol(a, n):
    """
    Calculates the Jacobi symbol (a/n) using the law of quadratic reciprocity. 
    Parameters:
        a: an integer
        n: an odd positive integer
    Returns:
        The value of the Jacobi symbol (a/n).
    """
    # The first terminating case. When a is equal to zero, the value of
    # the Jacobi symbol is also zero.
    if a == 0:
        return 0
    # The second terminating case. When a is equal to one, the value of
    # the Jacobi symbol is also one.
    elif a == 1:
        return 1
    # This part uses the law of quadratic reciprocity to compute the Jacobi
    # symbol for a non-terminal case. We first look at the case
    # where a is even.
    elif a % 2 == 0:
        # To implement this part, we use the second supplement of the law of
        # quadratic reciprocity.
        if n % 8 == 1 or n % 8 == 7:
            return jacobi_symbol(a//2, n)
        else:
            return -jacobi_symbol(a//2, n)
    # For this part we simply use the law of quadratic reciprocity to simplify
    # the recursively call the Jacobi_symbol function with smaller arguments.
    elif a % 4 == 3 and n % 4 == 3:
        return -jacobi_symbol(n % a, a)
    else:
        return jacobi_symbol(n % a, a)
