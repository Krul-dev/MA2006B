# -*- coding: utf-8 -*-
"""
ecc.py
Created on Wed May  9 20:02:08 2018

@author: raul

Basic functions and algorithms for implementing Elliptic Curve Cryptography
"""

from sympy import isprime

from cryptocalc.modular_arithmetic import divide_mod, exp_mod, jacobi_symbol

INFTY = "infty"

class EllipticCurve:
    def __init__(self, p, c1, c0):
        if not isprime(p):
            raise ValueError("The value of p must be a prime number.")

        a3 = exp_mod((c1 % p, p), 3)[0]
        b2 = exp_mod((c0 % p, p), 2)[0]
        discriminant = (-16 * (4 * a3 + 27 * b2)) % p

        if discriminant == 0:
            raise ValueError(
                "The discriminant of the elliptic curve is 0, so it is not a valid elliptic curve."
            )

        self.p = p
        self.c1 = c1 % p
        self.c0 = c0 % p
        self.discriminant = discriminant
        # Aliases commonly used in the short Weierstrass form:
        # y^2 = x^3 + a*x + b
        self.a = self.c1
        self.b = self.c0
    
    # This function computes the j-invariant of the elliptic curve
    def j_invariant(self):
        numerator = exp_mod(((-48 * self.c1) % self.p, self.p), 3)[0]
        return divide_mod((numerator, self.p), (self.discriminant, self.p))[0]

    def get_discriminant(self): 
        return self.discriminant

    # This function checks if a given point P belongs to the elliptic curve.
    def is_point_in_curve(self, P):
        if P != INFTY and (not isinstance(P, tuple) or len(P) != 2):
            raise TypeError("Point must be a tuple (x, y) or 'infty'.")

        if P == INFTY:
            return True

        x, y = P
        p = self.p
        x %= p
        y %= p

        lhs = exp_mod((y, p), 2)[0]
        rhs = (exp_mod((x, p), 3)[0] + (self.c1 * x) + self.c0) % p
        return lhs == rhs

    # This function calculates the denominator needed to double a point in an
    # elliptic curve. If the denominator is 0, then we know that the result
    # will be the point at infinity.
    def denominator_of_double(self, P):
        return (2 * P[1]) % self.p

    # This function calculates the denominator needed to add two points in an
    # elliptic curve. If the denominator is 0, then we know that the result
    # will be the point at infinity.
    def denominator_of_sum(self, P, Q):
        return (P[0] - Q[0]) % self.p

    # This function defines the sum of two points.
    def _sum(self, P, Q):
        x_1, y_1 = P
        x_2, y_2 = Q
        q = self.p
        m = divide_mod(((y_2 - y_1) % q, q), ((x_2 - x_1) % q, q))[0]
        x_3 = (m**2 - x_1 - x_2) % q
        y_3 = (m * (x_1 - x_3) - y_1) % q
        return (x_3, y_3)

    # This function defines the double of a point.
    def _double(self, P):
        x_1, y_1 = P
        q = self.p
        m = divide_mod(((3 * (x_1**2) + self.a) % q, q), ((2 * y_1) % q, q))[0]
        x_3 = (m**2 - 2 * x_1) % q
        y_3 = (m * (x_1 - x_3) - y_1) % q
        return (x_3, y_3)

    # This function implements the operation of taking the inverse of a point
    # in the elliptic curve.
    def inverse(self, P):
        if P == INFTY:
            return INFTY
        return (P[0], -P[1] % self.p)

    # This function implements the operation of doubling a point in an elliptic
    # curve.
    def double(self, P):
        if P == INFTY:
            return INFTY
        if self.denominator_of_double(P) == 0:
            return INFTY
        return self._double(P)

    # This function implements the operation of adding two points in an
    # elliptic curve.
    def addition(self, P, Q):
        if P == INFTY:
            return Q
        if Q == INFTY:
            return P
        if P == Q:
            return self.double(P)
        if self.denominator_of_sum(P, Q) == 0:
            return INFTY
        return self._sum(P, Q)

    # This function implements the operation of multiplying a point on the
    # elliptic curve by a given integer.
    def multiplication(self, m, P):
        if m == 0 or P == INFTY:
            return INFTY
        if m < 0:
            return self.multiplication(-m, self.inverse(P))
        if m % 2 == 0:
            return self.double(self.multiplication(m // 2, P))
        return self.addition(P, self.multiplication(m - 1, P))

    # This function computes the collection of points belonging to this
    # elliptic curve.
    # Note: For larger values of p, this operation is very intensive in terms
    # of time and storage space.
    def points(self):
        E_q = [INFTY]
        p = self.p
        for x in range(p):
            rhs = (pow(x, 3, p) + self.a * x + self.b) % p
            if jacobi_symbol(rhs, p) != -1:
                for y in range(p):
                    if pow(y, 2, p) == rhs:
                        E_q.append((x, y))
        return E_q

    # This function computes the order of a point P in the elliptic curve.
    def order(self, P):
        if P == INFTY:
            return 1
        current = P
        count = 1
        while current != INFTY:
            current = self.addition(current, P)
            count += 1
        return count
