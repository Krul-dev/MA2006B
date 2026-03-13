# -*- coding: utf-8 -*-
"""
Created on Sat May 19 10:57:00 2018

@author: raul
"""
from hashlib import sha256

def encode(sentence):
    encoded_sentence = 0
    for n in range(len(sentence)):
        encoded_sentence += ord(sentence[n])*(256**n)
    return encoded_sentence


def decode(encoded_sentence):
    decoded_sentence = ""
    while encoded_sentence != 0:
        decoded_sentence += chr(encoded_sentence % 256)
        encoded_sentence = encoded_sentence//256
    return decoded_sentence

def sha256_of_integer(n):
    length = (n.bit_length() + 7) // 8
    data = n.to_bytes(length, "little")
    digest = sha256(data).digest()
    return int.from_bytes(digest, "big")

def sha256_of_sentence(sentence):
    return sha256_of_integer(encode(sentence))
