# -*- coding: utf-8 -*-
"""
Created on Tue May 15 07:45:58 2018

@author: raul
"""


from cryptocalc.euclid_algorithm import gcd, fast_extended_gcd
from cryptocalc.encoding import encode, decode
from random import randint

from Crypto.Util import number

# RSA key generation function
def rsa_key_generation(lenght_of_prime_numbers):
    """
    Generate RSA key pair (public and private keys) based on the specified length of prime numbers.
    Parameters:
        lenght_of_prime_numbers (int): The bit length of the prime numbers to be generated.
    Returns:
        tuple: A tuple containing the public key (e, n) and the private key (d,n).
    """
    p = number.getPrime(lenght_of_prime_numbers)
    q = number.getPrime(lenght_of_prime_numbers)
    while p == q:
        q = number.getPrime(lenght_of_prime_numbers)

    n = p*q
    phi = (p-1)*(q-1)
    e = 65537 % phi
    while gcd(e, phi) != 1:
        e = randint(2, phi-2)
    d = fast_extended_gcd(phi, e)[1] % phi
    public_key = (e, n)
    private_key = (d, n)
    key_ring = (public_key, private_key)
    return key_ring


# RSA encryption function
def rsa_encryption(public_key, plain_message):
    """
    Encrypt a plain message using the RSA encryption algorithm.
    Parameters:
        public_key (tuple): The RSA public key (e, n) used for encryption.
        plain_message (int): The message to be encrypted, represented as an integer.
    Returns:
        int: The encrypted message, represented as an integer.
    """
    e = public_key[0]
    n = public_key[1]
    m = plain_message
    encrypted_message = pow(m, e, n)
    return encrypted_message


# RSA decryption function
def rsa_decryption(private_key, encrypted_message):
    """
    Decrypt an encrypted message using the RSA decryption algorithm.
    Parameters:
        public_key (tuple): The RSA public key (e, n) used for encryption.
        private_key (int): The RSA private key d used for decryption.
        encrypted_message (int): The message to be decrypted, represented as an integer.
    Returns:
        int: The decrypted message, represented as an integer.
    """
    d = private_key[0]
    n = private_key[1]
    c = encrypted_message
    decrypted_message = pow(c, d, n)
    return decrypted_message


# RSA text encryption function
# This function takes a plain text message, encodes it into an integer, and then encrypts it using the RSA encryption algorithm.
def rsa_text_encryption(public_key, plain_text_message):
    """
    Encrypt a plain text message using the RSA encryption algorithm.
    Parameters:
        public_key (tuple): The RSA public key (e, n) used for encryption.
        plain_text_message (str): The plain text message to be encrypted.
    Returns:
        int: The encrypted message, represented as an integer.
    """
    plain_message = encode(plain_text_message)
    encrypted_message = rsa_encryption(public_key, plain_message)
    return encrypted_message


# RSA text decryption function
# This function takes an encrypted message, decrypts it using the RSA decryption algorithm, and then decodes the resulting integer back into a plain text message.
def rsa_text_decryption(private_key, encrypted_message):
    """
    Decrypt an encrypted message using the RSA decryption algorithm and decode it back to plain text.
    Parameters:
        public_key (tuple): The RSA public key (e, n) used for encryption.
        private_key (int): The RSA private key d used for decryption.
        encrypted_message (int): The message to be decrypted, represented as an integer.
    Returns:
        str: The decrypted plain text message.
    """
    decrypted_message = rsa_decryption(private_key, encrypted_message)
    decrypted_text_message = decode(decrypted_message)
    return decrypted_text_message
