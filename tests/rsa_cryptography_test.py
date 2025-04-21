#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 14:45:29 2018

@author: raul
"""

from cryptocalc.rsa_cryptography import (rsa_text_encryption, rsa_text_decryption,
                                         rsa_key_generation, rsa_decryption)

from cryptocalc.encoding import encode


def main():
    key_ring = rsa_key_generation(100)
    public_key = key_ring[0]
    private_key = key_ring[1]

    print("\n")

    print("Test suit for the RSA cryptographic system with randomly "
          "generated keys: \n")
    print("  Private key =", private_key)
    print("  Public key =", public_key[1])
    print("  Parameter domain =", public_key[0], "\n")

    plain_text_message = (input("Please enter the message "
                                "that you want encrypted: "))
    print("")

    encoded_message = encode(plain_text_message)
    offset = public_key[0] - encoded_message
    encrypted_message = rsa_text_encryption(public_key, plain_text_message)
    decrypted_text_message = rsa_text_decryption(public_key, private_key,
                                                 encrypted_message)

    print("Your encoded message is: \n    ", encoded_message, "\n")
    print("Your encrypted message is: \n    ",  encrypted_message, "\n")
    print("Your decrypted message is: \n    ",
          decrypted_text_message, "\n")
    print("Your decrypted message in plain text is:\n    ",
          rsa_text_decryption(public_key, private_key, encrypted_message), "\n")
    print("It is within \n  ", offset,
          "\nunits of the required parameter domain.\n")


if __name__ == "__main__":
    main()
