# -*- coding: utf-8 -*-
"""
euclid_algorithm.py
Created on Mon Apr  2 12:13:46 2018

@author: raul
"""


def gcd(n, m):
    while m != 0:
        n, m = m, n % m
    return n


def extended_gcd(n, m):
    if m == 0:
        return (1, 0, n)
    else:
        return (extended_gcd(m, n % m)[1],
                extended_gcd(m, n % m)[0]-(n//m)*extended_gcd(m, n % m)[1],
                extended_gcd(m, n % m)[2])


def fast_extended_gcd(n, m):
    list_of_quotients = []
    q = 0
    r = 0
    while m != 0:
        q = n//m
        r = n % m
        list_of_quotients.append(q)
        n = m
        m = r
    a = 1
    b = 0
    for q in reversed(list_of_quotients):
        (a, b) = (b, a-q*b)
    extended_gcd = (a, b, n)
    return extended_gcd
