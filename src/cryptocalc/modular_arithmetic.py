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
    if m == 0:
        return (1, x[1])
    else:
        return multiply_mod(x, naive_exp_mod(x, m-1))


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
