#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-04-21
Description: 
"""

from cryptocalc import exp_mod
import os


# Example safe prime (2048-bit) from RFC 3526
RFC_3526_SAFE_PRIME = int(
    "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E08"
    "8A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B"
    "302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9"
    "A63A36210000000000090563", 16
)
# Sophie Germain prime (q = (p-1)//2)
RFC_3526_SOPHIE_PRIME = (RFC_3526_SAFE_PRIME - 1) // 2


def generate_private_key(q):
    """Return a uniformly random private key in [2**256, q-1].

    Args:
        q (int): A Sophie Germain prime that defines the upper bound.

    Raises:
        ValueError: If `q` is smaller than 2**384, which does not leave
            enough entropy for a secure private key.
    """
    # Validate q is big enough
    if q < 2**384:
        raise ValueError("q must be at least 2^384")
    # Calculate the byte length of q
    q_bytes = (q.bit_length() + 7) // 8  # Byte length of q
    while True:
        # Use os.urandom for cryptographic random bytes
        random_bytes = os.urandom(q_bytes)
        private_key = int.from_bytes(random_bytes, byteorder="big")
        if 2**256 <= private_key <= q - 1:
            return private_key


def diffie_hellman_public_key_generator(safe_prime, primitive_root, private_key):
    """
    Generate a public key using Diffie-Hellman key exchange.

    Parameters:
    safe_prime (int): A safe prime number.
    primitive_root (int): A primitive root modulo the safe prime.
    private_key (int): The private key of the user.

    Returns:
    int: The public key.
    """
    p = safe_prime
    g = primitive_root
    a = private_key
    public_key = exp_mod((g, p), a)
    # Return the first element of the tuple (the result of the exponentiation)
    return public_key[0]


def diffie_hellman_shared_key_generator(safe_prime, public_key, private_key):
    """
    Generate a shared key using Diffie-Hellman key exchange.

    Parameters:
    safe_prime (int): A safe prime number.
    public_key (int): The public key of the other user.
    private_key (int): The private key of the user.

    Returns:
    int: The shared key.
    """
    p = safe_prime 
    B = public_key
    a = private_key
    shared_key = exp_mod((B, p), a)
    # Return the first element of the tuple (the result of the exponentiation)
    return shared_key[0]
