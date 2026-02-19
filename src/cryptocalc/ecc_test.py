#!/usr/bin/python3
"""
Created on Wed May  9 20:02:08 2018
@author: raul
Basic functions and algorithms for implementing Elliptic Curve Cryptography
"""


from cryptocalc import EllipticCurve


def main():
    # We set our elliptic curve with parameters a=6 and b=23, that is, our
    # elliptic curve corresponds to the equation y^2 = x^3 + 6x + 23.
    a = 6
    b = 23

    # We set our base field to be F_103.
    p = 103
    curve = EllipticCurve(p, a, b)

    # We compute all the points of the elliptic curve.
    # We should notice that in general this is not practical, but in this very
    # small example, it can be done.
    E_q = curve.points()

    # As a base point, we choose the point P=(95,9)
    P = (95, 9)

    # We now create a list in which we store the passwords 20, 27 and 72
    list_of_passwords = [20, 27, 72]

    # We also create a list for the hashed passwords
    list_of_hashed_passwords = []

    # We now store the hash corresponding to the passwords 20, 27 and 72
    hash_of_password_1 = curve.multiplication(20, P)
    hash_of_password_2 = curve.multiplication(27, P)
    hash_of_password_3 = curve.multiplication(72, P)

    list_of_hashed_passwords.append(hash_of_password_1)
    list_of_hashed_passwords.append(hash_of_password_2)
    list_of_hashed_passwords.append(hash_of_password_3)

    # Now that we have done our computations, let's print the results:

    print("")
    print("This are the results of the test:  \n")
    print("We are working with the elliptic curve y^2=x^3+6x+23. \n")
    print("As a base field, we will use the field with 103 elements. \n")
    print("The list of all the points belonging to this ")
    print("elliptic curve is the following: \n")
    i = 0
    for entry in E_q:
        print(str(i+1) + ":", entry)
        i += 1

    print("")
    print("Now consider the following list of passwords: \n")
    print(list_of_passwords)
    print("")
    print("Since it is too risky to store the passwords in plain test,")
    print("we store instead the list of hashed passwords: \n")
    print(list_of_hashed_passwords)
    print("")


if __name__ == "__main__":
    main()
