#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-04-21
Description: 
"""

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
    # Validate q is big enough
    if q < 2**384:
        raise ValueError("q must be at least 2^256")
    # Calculate the byte length of q
    q_bytes = (q.bit_length() + 7) // 8  # Byte length of q
    while True:
        # Use os.urandom for cryptographic random bytes
        random_bytes = os.urandom(q_bytes)
        private_key = int.from_bytes(random_bytes, byteorder="big")
        if 2**256 <= private_key <= q - 1:
            return private_key


def main():
    q = RFC_3526_SOPHIE_PRIME
    a = generate_private_key(q)
    b = generate_private_key(q)

    print(f"Sophie Germain prime (q): {q}")
    print(f"Alice's private key (a): {a}")
    print(f"Bob's private key (b): {b}")


if __name__ == "__main__":
    main()
