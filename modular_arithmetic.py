
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 14:59:45 2018

@author: raul
"""

from euclid_algorithm import extended_gcd


# This module implements modular arithmetic operations
def simplify_mod(a, n):
    return (a % n, n)


def add_mod(x, y):
    return simplify_mod(x[0]+y[0], x[1])


def substact_mod(x, y):
    return simplify_mod(x[0]-y[0], x[1])


def multiply_mod(x, y):
    return simplify_mod(x[0]*y[0], x[1])


def divide_mod(x, y):
    return simplify_mod(x[0]*(extended_gcd(y[0], y[1])[0]), x[1])


def exp_mod(x, m):
    if m == 0:
        return (1, x[1])
    else:
        return multiply_mod(x, exp_mod(x, m-1))


def chinese_remainder(x, y):
    a = x[0]
    p = x[1]
    b = y[0]
    q = y[1]
    r = extended_gcd(p, q)[0]
    s = extended_gcd(p, q)[1]
    n = p*q
    z = b*p*r + a*q*s
    return simplify_mod(z, n)

