#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-04-21
Description: 
"""

from cryptocalc import exp_mod



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
    b = private_key
    shared_key = exp_mod((B, p), b)
    # Return the first element of the tuple (the result of the exponentiation)
    return shared_key[0]
