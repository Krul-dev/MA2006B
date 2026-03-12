# This file is required to make Python treat the directories as containing packages;


# src/cryptocalc/__init__.py

# Define the package version
from importlib.metadata import version as _version
__version__ = _version("MA2006B")

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
    naive_exp_mod,
    exp_mod,
    chinese_remainder,
    jacobi_symbol,
)

from cryptocalc.ecc import (
    EllipticCurve,
)

from cryptocalc.diffie_hellman import (
    diffie_hellman_public_key_generator,
    diffie_hellman_shared_key_generator,
)

from cryptocalc.rfc_specification import (
    RFC_3526_SAFE_PRIME,
    RFC_3526_SOPHIE_PRIME,
    generate_private_key,
)

from cryptocalc.sec_specification import (
    SECP256K1,
    generate_elliptic_private_key,
)

from cryptocalc.rsa_cryptography import (
    rsa_key_generation,
    rsa_encryption,
    rsa_decryption,
    rsa_text_encryption,
    rsa_text_decryption,
)

from cryptocalc.encoding import (
    encode,
    decode,
    sha256_of_integer,
    sha256_of_sentence,
)

from cryptocalc.elgamal import (
    elgamal_public_key_generator,
    elgamal_key_generation,
    elgamal_encryption,
    elgamal_decryption
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
    "naive_exp_mod",
    "exp_mod",
    "chinese_remainder",
    "jacobi_symbol",
    "diffie_hellman_public_key_generator",
    "diffie_hellman_shared_key_generator",
    "RFC_3526_SAFE_PRIME",
    "RFC_3526_SOPHIE_PRIME",
    "generate_private_key",
    "rsa_key_generation",
    "rsa_encryption",
    "rsa_decryption",
    "rsa_text_encryption",
    "rsa_text_decryption",
    "encode",
    "decode",
    "sha256_of_integer",
    "sha256_of_sentence",
    "elgamal_public_key_generator",
    "elgamal_key_generation",
    "elgamal_encryption",
    "elgamal_decryption",
    "EllipticCurve",
    "SECP256K1",
    "generate_elliptic_private_key",
]
