#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-04-21
Description:
"""

from cryptocalc import generate_private_key 
from cryptocalc.modular_arithmetic import exp_mod
from cryptocalc.euclid_algorithm import fast_extended_gcd
from cryptocalc.encoding import encode, decode
import os


def _uniform_random_below(upper_bound):
    """Return a uniform random integer in [0, upper_bound-1]."""
    if upper_bound <= 0:
        raise ValueError("upper_bound must be positive")

    num_bytes = (upper_bound.bit_length() + 7) // 8
    while True:
        candidate = int.from_bytes(os.urandom(num_bytes), byteorder="big")
        if candidate < upper_bound:
            return candidate


def _uniform_random_in_range(lower_bound, upper_bound):
    """Return a uniform random integer in [lower_bound, upper_bound]."""
    if lower_bound > upper_bound:
        raise ValueError("lower_bound must be <= upper_bound")

    width = upper_bound - lower_bound + 1
    return lower_bound + _uniform_random_below(width)

def elgamal_public_key_generator(safe_prime, primitive_root, private_key):
    """
    Generate a public key using ElGamal over Z/pZ.

    Parameters:
    safe_prime (int): A safe prime number.
    primitive_root (int): A primitive root modulo the safe prime.
    private_key (int): The private key x.

    Returns:
    int: The public component y = g^x mod p.
    """
    p = safe_prime
    g = primitive_root
    x = private_key
    public_key = exp_mod((g, p), x)
    return public_key[0]


def elgamal_key_generation(safe_prime, primitive_root):
    """
    Generate an ElGamal key pair.

    Parameters:
    safe_prime (int): Modulus p.
    primitive_root (int): Generator g.

    Returns:
    tuple: ((p, g, y), x) where y = g^x mod p.
    """
    p = safe_prime
    g = primitive_root
    x = _uniform_random_in_range(2, p - 2)
    y = elgamal_public_key_generator(p, g, x)
    public_key = (p, g, y)
    private_key = x
    key_ring = (public_key, private_key)
    return key_ring


def elgamal_encryption(public_key, plain_message):
    """
    Encrypt an integer with ElGamal.

    Parameters:
    public_key (tuple): (p, g, y).
    plain_message (int): Integer m with 0 <= m < p.

    Returns:
    tuple: Ciphertext (c1, c2).
    """
    p = public_key[0]
    g = public_key[1]
    y = public_key[2]
    m = plain_message

    if not 0 <= m < p:
        raise ValueError("plain_message must satisfy 0 <= plain_message < p")

    k = _uniform_random_in_range(2, p - 2)
    c1 = exp_mod((g, p), k)[0]
    s = exp_mod((y, p), k)[0]
    c2 = (m * s) % p
    encrypted_message = (c1, c2)
    return encrypted_message


def elgamal_decryption(public_key, private_key, encrypted_message):
    """
    Decrypt an ElGamal ciphertext.

    Parameters:
    public_key (tuple): (p, g, y).
    private_key (int): Private key x.
    encrypted_message (tuple): Ciphertext (c1, c2).

    Returns:
    int: Decrypted integer message.
    """
    p = public_key[0]
    x = private_key
    c1 = encrypted_message[0]
    c2 = encrypted_message[1]

    s = exp_mod((c1, p), x)[0]
    s_inverse = fast_extended_gcd(p, s)[1] % p
    decrypted_message = (c2 * s_inverse) % p
    return decrypted_message


def elgamal_text_encryption(public_key, plain_text_message):
    """Encode text to an integer and encrypt it with ElGamal."""
    plain_message = encode(plain_text_message)
    encrypted_message = elgamal_encryption(public_key, plain_message)
    return encrypted_message


def elgamal_text_decryption(public_key, private_key, encrypted_message):
    """Decrypt ElGamal ciphertext and decode it as text."""
    decrypted_message = elgamal_decryption(
        public_key, private_key, encrypted_message
    )
    decrypted_text_message = decode(decrypted_message)
    return decrypted_text_message
