#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-04-20
Description: 
"""

import numpy as np

# Constants for GF(4): {0, 1, x, x+1}, where x is the root of an irreducible polynomial
GF4_ELEMENTS = [0, 1, 2, 3]  # Corresponding to 0, 1, x, x+1
GF4_ADD = [[0, 1, 2, 3],  # Addition table in GF(4)
           [1, 0, 3, 2],
           [2, 3, 0, 1],
           [3, 2, 1, 0]]
GF4_MUL = [[0, 0, 0, 0],  # Multiplication table in GF(4)
           [0, 1, 2, 3],
           [0, 2, 3, 1],
           [0, 3, 1, 2]]

# Helper functions for GF(4) arithmetic


def gf4_add(a, b):
    return GF4_ADD[a][b]


def gf4_mul(a, b):
    return GF4_MUL[a][b]


# Simplified S-box (substitute bytes step)
SBOX = [0, 3, 1, 2]  # A simple permutation

# Inverse S-box
INV_SBOX = [0, 2, 3, 1]

# Key expansion for 2-round AES (simple XOR-based key schedule)


def key_expansion(key):
    round_keys = [key]
    for i in range(1, 3):  # 2 rounds
        # Simple addition for round keys
        round_key = [gf4_add(k, i) for k in round_keys[i-1]]
        round_keys.append(round_key)
    return round_keys

# SubBytes step


def sub_bytes(state):
    return [SBOX[byte] for byte in state]

# ShiftRows step (doesn't change rows in this simplified version)


def shift_rows(state):
    return state

# MixColumns step (simplified for GF(4))


def mix_columns(state):
    # Hardcoded MixColumns matrix multiplication
    mix_matrix = [[1, 2], [2, 1]]  # Simplified matrix over GF(4)
    new_state = [0] * len(state)
    for i in range(2):  # 2x2 matrix
        for j in range(2):
            new_state[i] ^= gf4_add(
                gf4_mul(mix_matrix[i][0], state[j * 2]),
                gf4_mul(mix_matrix[i][1], state[j * 2 + 1]),
            )
    return new_state

# AddRoundKey step


def add_round_key(state, round_key):
    return [gf4_add(byte, key) for byte, key in zip(state, round_key)]

# Encryption function


def encrypt(plaintext, key):
    state = plaintext
    round_keys = key_expansion(key)

    # Initial round key addition
    state = add_round_key(state, round_keys[0])

    # 2 rounds of AES
    for round_num in range(1, 3):
        state = sub_bytes(state)
        state = shift_rows(state)
        if round_num < 2:  # No MixColumns in the last round
            state = mix_columns(state)
        state = add_round_key(state, round_keys[round_num])

    return state


def main():
    # Example plaintext and key
    plaintext = [1, 2, 3, 0]  # Example 2x2 plaintext matrix
    key = [0, 1, 2, 3]       # Example key

    # Encrypt the plaintext
    ciphertext = encrypt(plaintext, key)
    print("plaintext:", plaintext)
    print("Key:", key)
    print("Ciphertext:", ciphertext)


# Example usage
if __name__ == "__main__":
    main()
