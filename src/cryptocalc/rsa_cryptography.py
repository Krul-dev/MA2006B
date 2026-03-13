# -*- coding: utf-8 -*-
"""
Created on Tue May 15 07:45:58 2018

@author: raul
"""


from cryptocalc.euclid_algorithm import gcd, fast_extended_gcd
from cryptocalc.encoding import encode, decode
from random import randint

from Crypto.Util import number


def rsa_key_generation(lenght_of_prime_numbers):
    p = number.getPrime(lenght_of_prime_numbers)
    q = number.getPrime(lenght_of_prime_numbers)
    n = p*q
    phi = (p-1)*(q-1)
    e = randint(2, phi-2)
    while gcd(e, phi) != 1:
        e = randint(2, phi-2)
    d = fast_extended_gcd(phi, e)[1] % phi
    public_key = (e, n)
    private_key = d
    key_ring = (public_key, private_key)
    return key_ring


def rsa_encryption(public_key, plain_message):
    e = public_key[0]
    n = public_key[1]
    m = plain_message
    encrypted_message = pow(m, e, n)
    return encrypted_message


def rsa_decryption(public_key, private_key, encrypted_message):
    n = public_key[1]
    c = encrypted_message
    d = private_key
    decrypted_message = pow(c, d, n)
    return decrypted_message


def rsa_text_encryption(public_key, plain_text_message):
    plain_message = encode(plain_text_message)
    encrypted_message = rsa_encryption(public_key, plain_message)
    return encrypted_message


def rsa_text_decryption(public_key, private_key, encrypted_message):
    decrypted_message = rsa_decryption(
        public_key, private_key, encrypted_message)
    decrypted_text_message = decode(decrypted_message)
    return decrypted_text_message
