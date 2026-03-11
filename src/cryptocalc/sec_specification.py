#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2026-03-11
Description: 
"""

import os

# This file contains the parameters for the curve secp256k1, which is widely used in cryptographic applications, including Bitcoin.
SECP256K1 = {
    "p": 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F,
    "a": 0,
    "b": 7,
    "G": (
        0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
        0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,
    ),
    "n": 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141,
    "h": 1,
}

# Private key generation for secp256k1 
def generate_elliptic_private_key(n):
    """Return a uniformly random private key in [2**128, n-1].

    Args:
        n (int): The order of the base point G, which defines
        the upper bound for the private key.

    Raises:
        ValueError: If `n` is smaller than 2**128, which may 
        be susceptible to brute-force attacks. A secure private key
        should have at least 128 bits of entropy.
    """
    # Validate q is big enough
    if n < 2**192:
        raise ValueError("n must be at least 2^192")
    # Calculate the byte length of n
    n_bytes = (n.bit_length() + 7) // 8  # Byte length of q
    while True:
        # Use os.urandom for cryptographic random bytes
        random_bytes = os.urandom(n_bytes)
        private_key = int.from_bytes(random_bytes, byteorder="big")
        if 2**128 <= private_key <= n - 1:
            return private_key
