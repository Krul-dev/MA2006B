# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 12:13:46 2018

@author: raul
"""

def gcd(n,m):
    if m==0:
        return n
    else:
        return gcd(m,n-(n//m)*m)


def extended_gcd(n,m):
    if m==0:
        return (1,0,n)
    else:
        return(extended_gcd(m,n%m)[1],extended_gcd(m,n%m)[0]-(n//m)*extended_gcd(m,n%m)[1],extended_gcd(m,n%m)[2])