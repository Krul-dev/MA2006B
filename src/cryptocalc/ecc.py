# -*- coding: utf-8 -*-
"""
ecc.py
Created on Wed May  9 20:02:08 2018

@author: raul

Basic functions and algorithms for implementing Elliptic Curve Cryptography
"""


from cryptocalc import divide_mod

# This function calculates the denominator needed to double a point in an
# elliptic curve. If the denominator is 0, then we now that the result will be
# the point at infinity.
def e_denominator_of_double(P, E, q):
    return (2*P[1]) % q


# This function calculates the denominator needed to add two points in an
# elliptic curve. If the denominator is 0, then we now that the result will be
# the point at infinity.
def e_denominator_of_sum(P, Q, E, q):
    return (P[0]-Q[0]) % q


# These functions provide the basic formulas for computing the sum of two
# points in an elliptic curve.
# This function defines the sum of two points.
def e_sum(P, Q, E, q):
    x_1 = P[0]
    y_1 = P[1]
    x_2 = Q[0]
    y_2 = Q[1]
    m = divide_mod(((y_2-y_1) % q, q), ((x_2-x_1) % q, q))[0]
    x_3 = (m**2-x_1-x_2) % q
    y_3 = (m*(x_1-x_3)-y_1) % q
    return (x_3, y_3)


# This function defines the double of a point.
def e_double(P, E, q):
    a = E[0]
    x_1 = P[0]
    y_1 = P[1]
    m = divide_mod(((3*(x_1**2) + a) % q, q), ((2 * y_1) % q, q))[0]
    x_3 = (m**2-2*x_1) % q
    y_3 = (m*(x_1-x_3)-y_1) % q
    return (x_3, y_3)


"""
These functions calculate the basic invariants associated to an Elliptic
curve
"""


# This function calculates the discriminant of an elliptic curve.
def discriminant(E):
    return -16*(4*(E[0]**3) + 27*(E[1]**2))


# This function calculates the j-invariant of an elliptic curve.
def j_invariant(E):
    return ((-48*E[0])**3)/discriminant(E)


"""
These functions implement the basic addition and doubling operators in an
elliptic curve
"""


# This function implements the operation of taking the inverse of a point in
# the elliptic curve.
# The value of P=(x,y) represents the point in the elliptic curve for which we
# want to compute the inverse.
# The value of q represents the order of the base field over which we are
# considering the points.
def elliptic_inverse(P, q):
    # We first consider the special case in which P is the point at infinity.
    if P == "infty":
        return "infty"
    # Here we consider the general case.
    else:
        return (P[0], -P[1] % 1)


# This function implements the operation of doubling a point in an elliptic
# curve.
# The value of P=(x,y) represents the point in the elliptic curve for which
# we want to compute the inverse.
# The value of E represents the parameters (a,b) that define the elliptic
# curve.
# The value of q represents the order of the base field over which we are
# considering the points.
def elliptic_double(P, E, q):
    # We first consider the special case in which P is the point at infinity.
    if P == "infty":
        return "infty"
    # Now we consider the case in which P is its own inverse, and hence
    # doubling it gives us the point at infinity.
    elif e_denominator_of_double(P, E, q) == 0:
        return "infty"
    # Here we consider the generic case.
    else:
        return e_double(P, E, q)


# This function implements the operation of adding two points in an elliptic
# curve.
# This function implements the operation of doubling a point in an elliptic
# curve.
# The value of P=(x,y) represents the point in the elliptic curve for which
# we want to compute the inverse.
# The value of E represents the parameters (a,b) that define the elliptic
# curve.
# The value of q represents the order of the base field over which we are
# considering the points.
def elliptic_addition(P, Q, E, q):
    # We first consider the special case in which P is the point at infinity.
    if P == "infty":
        return Q
    # We then consider the special case in which Q is the point at infinity.
    elif Q == "infty":
        return P
    # Now we consider the case in which the two points are equal. In this case
    # we call the doubling function to compute the result.
    elif P == Q:
        return elliptic_double(P, E, q)
    # If the denominator is 0, then we obtain the point at infinity.
    elif e_denominator_of_sum(P, Q, E, q) == 0:
        return "infty"
    # Here we consider the generic case.
    else:
        return e_sum(P, Q, E, q)


# This function implements the operation of multiplying a point on the elliptic
# curve by a given integer.
# This function implements the operation of doubling a point in an elliptic
# curve.
# The value of P=(x,y) represents the point in the elliptic curve for which we
# want to compute the inverse.
# The value of E represents the parameters (a,b) that define the elliptic
# curve.
# The value of q represents the order of the base field over which we are
# considering the points.
def elliptic_multiplication(m, P, E, q):
    # First we consider the case in which P is the point at infinity or m is
    # equal to 0 (mod q) in which case we obtain the point at infinity as a
    # result.
    if m % q == 0 or P == "infty":
        return "infty"
    # If m is negative, then we call the function again replacing m by -m and P
    # by its inverse.
    elif m < 0:
        return elliptic_multiplication(-m, elliptic_inverse(P, q))
    # If m is even, then we call the function again replacing m by m/2 and we
    # double the result.
    elif m % 2 == 0:
        return elliptic_double(elliptic_multiplication(m//2, P, E, q), E, q)
    # If m is odd, then we call the function again replacing m by m-1 and then
    # add the point P to the result obtained.
    else:
        return elliptic_addition(P, elliptic_multiplication(m-1, P, E, q),
                                 E, q)


# This function computes the collection of points belonging to a given elliptic
# curve.
# Note: For larger values of q, this operation is very intensive in terms of
# time and storage space.
def points_of_elliptic_curve(E, q):
    E_q = ["infty"]
    for x in list(range(q)):
        if jacobi_symbol((pow(x, 3, q)+E[0]*x+E[1]) % q, q) != -1:
            for y in list(range(q)):
                if pow(y, 2, q) == (pow(x, 3, q)+E[0]*x+E[1]) % q:
                    E_q.append((x, y))
    return E_q
