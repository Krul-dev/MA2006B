# This file is required to make Python treat the directories as containing packages;


# src/cryptocalc/__init__.py

# Importing constants and functions for public use
from cryptocalc.euclid_algorithm import (
    gcd,
    extended_gcd,
)

from cryptocalc.modular_arithmetic import (
    simplify_mod,
    add_mod,
    substract_mod,
    multiply_mod,
    divide_mod,
    exp_mod,
    chinese_remainder,
)

from cryptocalc.ecc import (
    jacobi_symbol,
    discriminant,
    elliptic_inverse,
    elliptic_double,
    elliptic_addition,
    elliptic_multiplication,
    points_of_elliptic_curve,
)

from cryptocalc.diffie–hellman import (
    diffie_hellman_public_key_generator,
    diffie_hellman_shared_key_generator,
)


# Define public API
__all__ = [
    "gcd",
    "extended_gcd",
    "simplify_mod",
    "add_mod",
    "substract_mod",
    "multiply_mod",
    "divide_mod",
    "exp_mod",
    "chinese_remainder",
    "jacobi_symbol",
    "discriminant",
    "elliptic_inverse",
    "elliptic_double",
    "elliptic_addition",
    "elliptic_multiplication",
    "points_of_elliptic_curve",
    "diffie_hellman_public_key_generator",
    "diffie_hellman_shared_key_generator",
]
