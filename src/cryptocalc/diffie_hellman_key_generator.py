#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-04-21
Description: 
"""

from cryptocalc import RFC_3526_SAFE_PRIME, RFC_3526_SOPHIE_PRIME, generate_private_key

def main():
    """Generate two Diffie-Hellman private keys and print them."""
    p = RFC_3526_SAFE_PRIME
    q = RFC_3526_SOPHIE_PRIME
    a = generate_private_key(q)
    b = generate_private_key(q)

    print(f"Safe prime (p): {p}")
    print(f"Sophie Germain prime (q): {q}")
    print(f"Alice's private key (a): {a}")
    print(f"Bob's private key (b): {b}")

if __name__ == "__main__":
    main()
