#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-04-21
Description: 
"""

from Crypto.Random import get_random_bytes
from Crypto.Util.number import bytes_to_long

# Example safe prime (2048-bit)
# In practice, use a standardized safe prime from RFC 3526 or another trusted source
p = int(
    "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E08"
    "8A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B"
    "302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9"
    "A63A36210000000000090563", 16
)
q = (p - 1) // 2  # Subgroup order (approximately 1024 bits for a 2048-bit prime)

# Generate private key 'a'


def generate_private_key(q):
    # Determine byte length of q
    q_bytes = (q.bit_length() + 7) // 8  # Convert bit length to byte length
    while True:
        # Generate random bytes of size q
        random_bytes = get_random_bytes(q_bytes)
        # Convert bytes to long integer
        private_key = bytes_to_long(random_bytes)
        # Ensure private key is in the range [2^256, q-1]
        if 2**256 <= private_key <= q - 1:
            return private_key


def main():
    # Generate private keys for Alice (a) and Bob (b)
    a = generate_private_key(q)
    b = generate_private_key(q)

    # Print the private keys
    print(f"Alice's private key (a): {a}")
    print(f"Bob's private key (b): {b}")


if __name__ == "__main__":
    main()
